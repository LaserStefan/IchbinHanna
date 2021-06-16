# Analysis of Tweets for the #IchBinHannah Campaign

Autor_innen: Jana Lasser, Stefan Laser, Migle Bareikyte, Miria Blöchel, Tim Schatto-Eckrodt, Elen Le Foll, Christian Funk, David Adler

[![CC BY 4.0][cc-by-shield]][cc-by]

## Data  

### Included Datasets
So far, we included data for four hashtags of interest, from the time period between 2018-01-01 to 2021-06-13, stored in individual data files:
* **#WissZeitVG**: this is the "baseline" hashtag, referring to the law that governs academic employment in Germany. There was constant tweet activity with this hashtag throughout.
* **#FristIstFrust**: this hashtag became popular in early 2019 and has been around ever since.
* **#95vsWissZeitVG**: this hashtag became popular in mid 2020 and has been around ever since.
* **#IchBinHanna**: this hashtag refers to "Hanna" from a rather condescending [video](https://www.bmbf.de/de/media-video-16944.html) published by the German ministry for education and research back in 2018. In June 2021, the video was "rediscovered" and caused a wave of activity under the #IchBinHannah hashtag on Twitter.
* **#ACertainDegreeOfFlexibility**: Hashtag that ocurred shortly before the #IchBinHanna wave and was overtaken by it.
* **#IchBinJelena**
* **#IchBinMelek**
* **IchBinNichtHanna**
* In addition, the data set ```video_url``` includes all Tweets that directly contain the link https://www.bmbf.de/de/media-video-16944.html that points to the video from the ministry.

All data sets were downloaded using twarc, using the script ```code/get_data.ipynb``` (see section [Getting data from Twitter](#getting-data-from-twitter)). The respecitve queries for each data set are stored in the folder ```code/queries```.

In this repository we store only the Tweet IDs and Conversation IDs of the Tweets and conversations that were included in the data analysis. We do not store full tweets, due to restrictions in the Twitter terms of use. Using the Tweet IDs stored in ```data/tweet-IDs```, you can "rehydrate" the corresponding tweets, using for example [twarc](https://scholarslab.github.io/learn-twarc/06-twarc-command-basics#rehydrate-a-dataset) by typing  

```twarc2 hydrate tweet_ids.txt > tweets_hydrated.jsonl```  

in your command line. Similarly, by using the [twarc conversations](https://twarc-project.readthedocs.io/en/latest/twarc2/#conversations) utility, you can retrieve all Tweets belonging to a converation ID  

```twarc2 conversations conversation_ids.txt conversations.jsonl```

### Getting data from Twitter
Data from Twitter can be scraped via the [Twitter v2 API](https://developer.twitter.com/en/docs/twitter-api/early-access). To get access to full archival search (i.e. be able to search for Tweets that were tweeted longer than one week ago), you will need ["academic access"](https://developer.twitter.com/en/products/twitter-api/academic-research) to the twitter API. Once you have access, scraping tweets is fairly easy, using for example the command line tool [twarc](https://twarc-project.readthedocs.io/en/latest/twarc2/#conversations). We provide scripts that scrape the data for our hashtag(s) of interest in the folder ```code```(see ```basic-twarc-code.txt``` and ```get_data.ipynb```).


## Analysis
To analyse the data, I recommend converting the json line files into ```.csv``` files. This can be done using [twarc-csv](https://github.com/DocNow/twarc-csv), an extension for twarc. Conversion to .csv is also included in the script ```code/get_data.ipynb```. You will have to install the twarc-csv extension before it works, though.  

The script ```analyse_data.ipynb``` includes some basic exploration of the number of tweets for each of the hashtags over time, and the number of unique users engaged in each hashtag "wave". Visualizations that result from the analysis are stored in the folder ```plots```.

## Qualitative analysis
To facilitate the qualitative analysis process, a searchable and filterable table was created. It can be accessed via ```SearchableTable.html``` and should work interactively in any browser. The code used to create it can be found under ```code/SearchableTable.Rdm``` and the underlying data is stored in ```data/tweets_unique_keyinfo.rds```. The code used to create the underlying dataset is stored in the private OSF repository because it includes the full twitter metadata.

### Network Analysis
To get a sense of the Twitter interaction and its devisions, tools of network visualization can be used. Drawing on the open graph programm ["Gephi"](https://gephi.org/), the file ```Hanna.csv``` was imported and correlations drawn between ```user``` and ```in_reply_to_user.username```. The Force Atlas2 algorithm with basic options (no overlap and a few colours) was used. In ```plots```, two examples show the center of the network (a first zoom) and one seperate instance of interactions (a second zoom, showing the infamous Don Alphonso).


This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
