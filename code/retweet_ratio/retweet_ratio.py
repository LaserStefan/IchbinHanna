
import jsonlines
import lzma
import sys


def main(arguments):
    path = arguments[1]
    number_of_tweets = 0
    number_of_retweets = 0
    number_of_quotes = 0
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
    retweet_ratio = round(number_of_retweets/number_of_tweets*100, 2)
    retweets_and_quotes = number_of_retweets + number_of_quotes
    retweetandquote_ratio = round(retweets_and_quotes/number_of_tweets*100, 2)
    print("For file:" + path)
    print("Tweets gesamt: " + str(number_of_tweets))
    print("Retweets: " + str(number_of_retweets))
    print("quotes: " + str(number_of_quotes))
    print("Retweet ratio: " +  str(retweet_ratio))
    print("Ratio of retweets and quotes: " + str(retweetandquote_ratio))



if __name__ == '__main__':
    main(sys.argv)
