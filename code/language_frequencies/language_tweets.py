import json
import os
import jsonlines
import lzma
from collections import Counter
import sys
from datetime import datetime
import csv

directory = os.getcwd()
# x = input("Enter File (F) or Directory (D)")

def main(arguments):
    languageArray = []
    if arguments[1]=="file":
        path = arguments[2]
        languageArray = tweet_languages_in_file(path)
    elif arguments[1]=="folder":
        path = arguments[2]
        languageArray = tweet_languages_in_folder(path)
    elif arguments[1]=="-h":
        print("Form: python3 language_tweets.py [Arg1] [path to file or folder]\n Args1:\n folder -> alle Datein im Ordner\n file -> alle Tweets in einer Datei")
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
    # sums all language codes
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
    with open(csvfile, "w") as file:
      fieldnames = ["Country", "Frequency", "%"]
      writer = csv.writer(file)
      writer.writerow(["Language frequences for file or folder: ", sourcename])
      writer.writerow(fieldnames)
      for key, value in counts.items():
          relative_frequency = value/sumcounts*100
          writer.writerow([key, value, round(relative_frequency, 2)])
    # try:
    #     with open(csvfile, "w") as file:
    #       fieldnames = ["Country", "Frequency"]
    #       writer = csv.writer(file)
    #       writer.writerow(["Language frequences for file or folder: ", sourcename])
    #       writer.writerow(fieldnames)
    #       writer.writerows(counts.items() + "," + float(counts.value()/sumcounts))
    # except:
    #       print("Could not build csv-file.")

if __name__ == '__main__':
    main(sys.argv)
