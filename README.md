# Analysis of Tweets for the #IchBinHannah Campaign

## Data  

### Included Datasets
So far, we included data for four hashtags of interest, from the time period between 2018-01-01 to 2021-06-13, stored in individual data files:
* **#WissZeitVG**: this is the "baseline" hashtag, referring to the law that governs academic employment in Germany. There was constant tweet activity with this hashtag throughout.
* **#FristIstFrust**: this hashtag became popular in early 2019 and has been around ever since.
* **95vsWissZeitVG**: this hashtag became popular in mid 2020 and has been around ever since.
* **IchBinHannah**: this hashtag refers to "Hannah" from a rather condescending [video](https://www.bmbf.de/de/media-video-16944.html) published by the German ministry for education and research back in 2018. In June 2021, the video was "rediscovered" and caused a wave of activity under the #IchBinHannah hashtag on Twitter.
* In addition, the data set ```video_url``` includes all Tweets that directly contain the link https://www.bmbf.de/de/media-video-16944.html that points to the video from the ministry.

All data sets were downloaded using twarc, using the script ```code/get_data.ipynb``` (see section [Getting data from Twitter](#getting-data-from-twitter)). The respecitve queries for each data set are stored in the folder ```code/queries```.

Data sets are stored as ```.xs``` compressed ```.jsonl``` files in the folder ```data```. Before using them, you will have to decompress them (under Linux, you can decompress .xs files by running ```xs -d filename```, under Windows, you can use for example [winZIP](https://www.winzip.com/win/de/landing/download-winzip-v1.html?gclid=CjwKCAjw2ZaGBhBoEiwA8pfP_p6NpBeHAF8yRpFt9TPNt0t-cEve6TX22LIs7NV8YDNZu8_ABqKrhxoCYEMQAvD_BwE)).

### Getting data from Twitter
Data from Twitter can be scraped via the [Twitter v2 API](https://developer.twitter.com/en/docs/twitter-api/early-access). To get access to full archival search (i.e. be able to search for Tweets that were tweeted longer than one week ago), you will need ["academic access"](https://developer.twitter.com/en/products/twitter-api/academic-research) to the twitter API. Once you have access, scraping tweets is fairly easy, using for example the command line tool [twarc](https://twarc-project.readthedocs.io/en/latest/twarc2/#conversations). We provide scripts that scrape the data for our hashtag(s) of interest in the folder ```code```(see ```basic-twarc-code.txt``` and ```get_data.ipynb```).

### Conversations
It would be interesting to analyse all conversations that were kicked-off by a tweet containing one of our hashtags of interest. Conversations can be scraped using ```twarc2 conversations [OPTIONS] [INFILE] [OUTFILE]```. Conversation IDs for all Tweets scraped for every one of the hasthtags of interest are stored in the folder ```data/converstion_IDs```. It is recommended to split the files into chunks of 1000 or less IDs per twarc request.

## Analysis
To analyse the data, I recommend converting the json line files into ```.csv``` files. This can be done using [twarc-csv](https://github.com/DocNow/twarc-csv), an extension for twarc. Conversion to .csv is also included in the script ```code/get_data.ipynb```. You will have to install the twarc-csv extension before it works, though.  

The script ```analyse_data.ipynb``` includes some basic exploration of the number of tweets for each of the hashtags over time, and the number of unique users engaged in each hashtag "wave". Visualizations that result from the analysis are stored in the folder ```plots```.