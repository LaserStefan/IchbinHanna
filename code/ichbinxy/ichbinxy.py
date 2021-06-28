# Author: David Adler
# Versoin 1.0 from 28.6.2021
# as part of the Ich bin Hanna-Projekct
# Licence: CC BY 4.0
# For details on the licence and project see: https://github.com/LaserSteff/IchbinHanna


import jsonlines
import lzma
import os
import sys
import csv
import re
from nltk.corpus import stopwords
from collections import Counter

def main(arguments):
    path = arguments[1]
    directory = os.getcwd()
    my_stopwords = get_stopwords(directory)
    # runs function get_names which returns array of names
    listofnames = get_names(path, my_stopwords)
    # runs function save_to_csv which saves names as csv-file in subdirectory /results
    save_to_csv(listofnames, directory, type="names")
    frequency_list = get_name_frequencies(listofnames)
    save_to_csv(frequency_list, directory, type="freq")
    sys.exit(0) # ends script

# creates and returns stopwords from german stopwords by nltk and added stopwords in subdirectory
# /resources txt file
def get_stopwords(directory):
    directory = directory
    german_stopwords = stopwords.words("german")
    # appends manually added stopwords from file not_names_stopwords.txt in subdirectory /resources
    my_stopwords = german_stopwords
    not_names_stopwords_path = directory + "/resources/not_names_stopwords.txt"
    try:
        with open(not_names_stopwords_path, "r") as sw:
            Lines = sw.read().splitlines() # reads per line and exludes \n
            for line in Lines:
                my_stopwords.append(line)
    except:
        print("could not create not_names_stopwords. check if file not_names_stopwords.txt exists at subdirectory /resources")
    return(my_stopwords)

# creates list of names after "ich bin" from a jsonl.xz file based on twitter API v2
def get_names(path, my_stopwords):
    path = path
    my_stopwords = my_stopwords
    listofnames = []
    this_name = ""
    ich_bin = "ich bin"
    replace_signs_test = r"[^A-Za-zÀ-ÿ]" # excludes all non letters, keeps diacritics
    if path.endswith(".jsonl.xz"):
        # decompress file
        with lzma.open(path, "rb") as jsonlentry:
            # open file with jsonlines
            reader = jsonlines.Reader(jsonlentry)
            for obj in reader:
                for entry in obj["data"]:
                    # Retweets will not be taken into account
                    if "referenced_tweets" in entry and \
                        entry["referenced_tweets"][0]["type"]=="retweeted":
                            pass
                    else:
                        # text lower
                        # Get word after "Ich bin" and append to dictionary
                        if "ich bin" in entry["text"].lower():
                            tweet_text = entry["text"].lower()
                            # Delete numbers and interpunction from tweet text (substitute interpunction with " ")
                            tweet_text = re.sub(replace_signs_test, " ", tweet_text)
                            after_ich_bin = tweet_text.partition(ich_bin)[2]
                            this_name = after_ich_bin.split()[0]
                            if not this_name in my_stopwords:
                                #if not this_name in not_names_stopwords:
                                listofnames.append(this_name)
    return(listofnames)

# makes frequency list out of list of names
def get_name_frequencies(listofnames):
    listofnames = listofnames
    # get amount of all names
    sumcounts = len(listofnames)
    frequency_list = Counter(listofnames)
    return(frequency_list)

# writes names list or frequency list (depending on "type") into csv file
def save_to_csv(dictionary, directory, type):
    dictionary = dictionary
    directory = directory
    # checks if subdirectory "results" exists, otherwise creates it
    if not os.path.exists("results"):
        os.makedirs("results")
    path_names = directory + "/results/names.csv"
    path_names_freq = directory + "/results/names_freq.csv"
    # save listofnames into csv
    if type=="names":
        try:
            with open(path_names, "w") as file:
                fieldnames = ["names"]
                writer = csv.writer(file)
                #writer.writerow(["Language frequences for file or folder: ", sourcename])
                writer.writerow(fieldnames)
                for name in dictionary:
                    writer.writerow([name])
        except:
            print("Could not build names csv-file.")
    # saves frequency list into csv file
    if type=="freq":
        try:
            with open(path_names_freq, "w") as file:
              fieldnames = ["names", "freq"]
              writer = csv.writer(file)
              writer.writerow(fieldnames)
              for name, value in dictionary.items():
                  writer.writerow([name, value])
        except:
            print("Could not build csv-file.")


if __name__ == '__main__':
    main(sys.argv)
