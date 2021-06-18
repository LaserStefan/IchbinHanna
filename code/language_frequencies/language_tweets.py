import json
import os
import jsonlines
import lzma
from collections import Counter
import sys
from datetime import datetime
from defusedcsv import csv #avoid csv code injection (in case the data source is not reliable)

directory = os.getcwd()

def main(arguments):
    languageArray = []
    if arguments[1]=="file":
        path = arguments[2]
        # calls tweet_languages_in_file for the file-path given when starting the script, gets array of language codes
        languageArray = tweet_languages_in_file(path)
    elif arguments[1]=="folder":
        path = arguments[2]
        # calls tweet_languages_in_folder for the folder-path given when starting the script,  gets array of language codes
        languageArray = tweet_languages_in_folder(path)
    elif arguments[1]=="-h" or arguments[1]=="--help":
        print("Syntax: python3 language_tweets.py [ARGUMENTS] [PATH TO FILE OR FOLDER]\n ARGUMENTS:\n folder -> gets language count from all .json.xs files of the given folder\n file -> gets language count from a specific .jsonl.xs file")
        quit()
    else:
        print("You have entered arguments, that make no sense to me")
        quit()
    language_count(languageArray, path)
    quit()



def tweet_languages_in_file(filepath):
    path = filepath
    #print("path: " + path)
    languageArray = []
    if path.endswith(".jsonl.xz"):
        with lzma.open(path, "rb") as jsonlentry:
            # opens file with jsonlines
            reader = jsonlines.Reader(jsonlentry)
            for obj in reader:
                for entry in obj["data"]:
                    if not "referenced_tweets" in entry or entry["referenced_tweets"][0]["type"]!="retweeted":
                        #if not eintrag["type"]=="retweeted":
                        if "lang" in entry:
                            #print(obj.data.entity["lang"])
                            #  if not obj["lang"]=="":
                            languageArray.append(entry["lang"])
                        else:
                            print("lang does not exist")
    return(languageArray)


def tweet_languages_in_folder(folderpath):
    path = folderpath
    print("path:" + path)
    languageArray = []
    for entry in os.scandir(path):
        # selects all files that end with .jsonl.gz
        if entry.path.endswith(".jsonl.xz") and entry.is_file():
            # unzips file so we can work with it
            with lzma.open(entry, "rb") as jsonlentry:
                # opens file with jsonlines
                reader = jsonlines.Reader(jsonlentry)
                for obj in reader:
                    for entry in obj["data"]:
                        if not "referenced_tweets" in entry or entry["referenced_tweets"][0]["type"]!="retweeted":
                            #if not eintrag["type"]=="retweeted":
                            if "lang" in entry:
                                #print(obj.data.entity["lang"])
                                #  if not obj["lang"]=="":
                                languageArray.append(entry["lang"])
                            else:
                                print("lang does not exist")
    return(languageArray)

def language_count(languageArray, filepath):
    # gives the amount of all language codes
    sumcounts = len(languageArray)
    # creates a counter with absolute frequencies
    counts = Counter(languageArray)
    #timestamp to make filenames unique
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    #checks if folder for results exists, if not creates it
    if not os.path.exists("lf_results"):
        os.makedirs("lf_results")
    csvfile = directory + f"/lf_results/lang-freq_{timestamp}.csv"
    sourcename = filepath
    und_count = 0
    # writes counts dictionary into csv file
    try:
        with open(csvfile, "w") as file:
          fieldnames = ["Country", "Frequency", "%"]
          writer = csv.writer(file)
          writer.writerow(["Language frequences for file or folder: ", sourcename])
          writer.writerow(fieldnames)
          for key, value in counts.items():
            relative_frequency = value/sumcounts*100
            writer.writerow([key, value, round(relative_frequency, 2)])      
    except:
        print("Could not build csv-file.")


if __name__ == '__main__':
    main(sys.argv)
