# Plot: Tweet types compared

Authors: Jana Lasser, Stefan Laser, Migle Bareikyte, Maria Blöchl, Tim Schatto-Eckrodt, Elen Le Foll, Christian Funk, David Adler

[![CC BY 4.0][cc-by-shield]][cc-by]

[This script is part of the „Analysis of Tweets for the #IchBinHannah Campaign“ project. For more details and licence see: https://github.com/LaserSteff/-IchbinHanna/blob/main/README.md

## Plot

![plot](https://github.com/LaserSteff/-IchbinHanna/blob/main/plots/tweet_types_compared/tweet_types_compared_21-06-21.png)

## Additional information

### Values for #95vsWissZeitVG
```
Relative values
path: 95vsWissZeitVG.jsonl.xz
abolute_tweets: 13726
retweets: 82.52222060323474
quotes: 7.627859536645781
replies: 3.853999708582253
new_tweets: 5.995920151537228
```
### Values for #IchBinHanna
```
Relative values
path: IchBinHanna.jsonl.xz
abolute_tweets: 38762
retweets: 79.57793715494557
quotes: 5.417677106444456
replies: 4.893968319488159
new_tweets: 10.11041741912182
```

## Intrepretation

Compared with former campaigns on labour conditions in science the #IchBinHanna campaign is characterized by a more active base. Not only is the total amount of tweets higher, but the percentage of “new tweets”, tweets that are neither mere retweets, quotes or answers increased, too. 

## Version
25.6.2021

## Datasource

The plot has been created based on the Updated data from 21.06.2021.
It uses the collected data for #95vsWissZeitVG and #IchBinHanna.
For more information on the queries, see: https://github.com/LaserSteff/IchbinHanna/tree/main/code/queries

## Used code and scripts

The plot is based on the `retweet_ratio.py` script which returns numbers and ratios of tweet types for a file and the `tweet_types_compared.ipynb` which compares two files and returns numbers, ratios an the given plot.

Both scripts can be found here: 


This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
