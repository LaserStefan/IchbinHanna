
import jsonlines
import lzma
import sys


def main(arguments):
    path = arguments[1]
    freq_dict = get_freq(path)
    rel_freq_dict = get_rel_freq(freq_dict)
    print("\n")
    print("Absolute values")
    print(str(freq_dict))
    for key, value in freq_dict.items():
        print(key + ": " + str(value))
    print("\n")
    print("Relative values")
    for key, value in rel_freq_dict.items():
        print(key + ": " + str(value))
    print("\n")
    print(str(rel_freq_dict))

def get_freq(path):
    path = path
    number_of_tweets = 0
    number_of_retweets = 0
    number_of_quotes = 0
    number_of_replies = 0
    new_tweets = 0
    freq_dict = dict()
    if path.endswith(".jsonl.xz"):
        with lzma.open(path, "rb") as jsonlentry:
            # opens file with jsonlines
            reader = jsonlines.Reader(jsonlentry)
            for obj in reader:
                for entry in obj["data"]:
                    number_of_tweets += 1
                    if "referenced_tweets" in entry:
                        if entry["referenced_tweets"][0]["type"]=="retweeted":
                            number_of_retweets += 1
                        if entry["referenced_tweets"][0]["type"]=="quoted":
                            number_of_quotes += 1
                        if entry["referenced_tweets"][0]["type"]=="replied_to":
                            number_of_replies += 1
    new_tweets = number_of_tweets - number_of_retweets - number_of_quotes - number_of_replies
    freq_dict["path"] = path
    freq_dict["all_tweets"] = number_of_tweets
    freq_dict["retweets"] = number_of_retweets
    freq_dict["quotes"] = number_of_quotes
    freq_dict["replies"] = number_of_replies
    freq_dict["new_tweets"] = new_tweets

    return(freq_dict)

def get_rel_freq(freq_dict):
    freq_dict = freq_dict
    rel_freq_dict = dict()
    rel_freq_dict["path"] = freq_dict["path"]
    rel_freq_dict["abolute_tweets"] = freq_dict["all_tweets"]
    rel_freq_dict["retweets"] = freq_dict["retweets"]/freq_dict["all_tweets"]*100
    rel_freq_dict["quotes"] = freq_dict["quotes"]/freq_dict["all_tweets"]*100
    rel_freq_dict["replies"] = freq_dict["replies"]/freq_dict["all_tweets"]*100
    rel_freq_dict["new_tweets"] = freq_dict["new_tweets"]/freq_dict["all_tweets"]*100
    sum_of_freq = rel_freq_dict["retweets"] + rel_freq_dict["quotes"] + rel_freq_dict["replies"] + rel_freq_dict["new_tweets"]

    return(rel_freq_dict)


# Functions for calling frequencies from outside of the script
def tweet_ratios_abs(path):
    path = path
    freq_dict = dict()
    freq_dict = get_freq(path)
    return(freq_dict)

def tweet_ratios_rel(path):
    path = path
    freq_dict = get_freq(path)
    rel_freq_dict = get_rel_freq(freq_dict)
    return(rel_freq_dict)




if __name__ == '__main__':
    main(sys.argv)
