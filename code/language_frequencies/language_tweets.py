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
        sourcepath = arguments[2]
        # calls tweet_languages_in_file for the file-path given when starting the script, gets array of language codes
        languageArray = tweet_languages_in_file(sourcepath)
    elif arguments[1]=="folder":
        sourcepath = arguments[2]
        # calls tweet_languages_in_folder for the folder-path given when starting the script,  gets array of language codes
        languageArray = tweet_languages_in_folder(sourcepath)
    elif arguments[1]=="-h" or arguments[1]=="--help":
        print("Syntax: python3 language_tweets.py [ARGUMENTS] [PATH TO FILE OR FOLDER] \nARGUMENTS:\n folder -> gets language count from all .json.xs files of the given folder\n file -> gets language count from a specific .jsonl.xs file\n --help -> gives syntax")
        quit()
    else:
        print("You have entered arguments, that make no sense to me")
        quit()
    language_count(languageArray, sourcepath)
    quit()

######## FUNCTIONS #########
def tweet_languages_in_file(filepath):
    entry = filepath
    print(f"Language frequencies for file: {entry}")
    languageArray = []
    if entry.endswith(".jsonl.xz"):
        get_lang_from_entry(entry, languageArray)
    return(languageArray)


def tweet_languages_in_folder(folderpath):
    folderpath=folderpath
    print(f"Language frequencies for folder: {folderpath}")
    languageArray = []
    for entry in os.scandir(folderpath):
        # selects all files that end with .jsonl.gz
        if entry.path.endswith(".jsonl.xz") and entry.is_file():
            get_lang_from_entry(entry, languageArray)
    return(languageArray)


def get_lang_from_entry(entry, languageArray):
    # unzips file so we can work with it
    number_of_retweets = 0
    no_lang = 0
    with lzma.open(entry, "rb") as jsonlentry:
        # opens file with jsonlines
        reader = jsonlines.Reader(jsonlentry)
        for obj in reader:
            for entry in obj["data"]:
                if not "referenced_tweets" in entry or entry["referenced_tweets"][0]["type"]!="retweeted":
                    if "lang" in entry:
                        languageArray.append(entry["lang"])
                    else:
                        print("lang does not exist")
                        no_lang += 1
                else:
                    number_of_retweets += 1
    return(languageArray)


def language_count(languageArray, sourcepath):
    sourcename = sourcepath
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
