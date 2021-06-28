# Plot: „Ich bin xy“  Wordcloud

Authors: Jana Lasser, Stefan Laser, Migle Bareikyte, Maria Blöchl, Tim Schatto-Eckrodt, Elen Le Foll, Christian Funk, David Adler

[![CC BY 4.0][cc-by-shield]][cc-by]

This plot is part of the „Analysis of Tweets for the #IchBinHannah Campaign“ project. For more details and licence see: https://github.com/LaserSteff/-IchbinHanna/blob/main/README.md

## Plot

### Simple wordcloud
![wordcloud](https://github.com/LaserSteff/-IchbinHanna/blob/main/plots/ichbinxy/wordcloud_names_21-06-08.png)

### Hanna shaped wordcloud
![wordcloud](https://github.com/LaserSteff/-IchbinHanna/blob/main/plots/ichbinxy/wordcloud_names_hanna_21-06-28.png)

## Additional information
The plots are base on .csv files with names and frequencies. These give a more complete and sound impression of the appearance of names within the formula „Ich bin [NAME]“. The corresponding table can be found here:
https://github.com/LaserSteff/-IchbinHanna/tree/main/tables/ichbinxy


## Intrepretation

Based on the hastag #IchBinHanna many academics used the formula „Ich bin [name]“ to introduce very personal experiences with academic labour conditions. The names given can give a short impression of the diversity of voices that came forward during the campaign. There are 385 names in total. While a small amount of names is occuring multiple times the vast majority of names does only occure once or twice (333). Please note that retweets have been excluded from the count of names, so that the wordcloud represents the amount of tweets that have been produced using one name rather than the distribution and visibility of the tweets.

Of course the list of names can only give a very rough view on one aspect of diversity in the #IchBinHanna discourse. We work on a more close analysis of the hastags #IchBinJelena and #IchBinMelek to fruther understand diversity in the campaign for better academic labour conditions.

## Version
28.6.2021

## Datasource

The plot has been created based on the Updated data from 27.06.2021.
It uses the data from the #IchBinHanna dataset.
For more information on the queries, see: https://github.com/LaserSteff/IchbinHanna/tree/main/code/queries

## Used code and scripts

The python script `ichbinxy.py` is used to produce a table of names and a table of names and frequencies, which can be found under /tables/ichbinxy.
Retweets are excluded from the the analysis, so that the image represen

The python based jupyter notebook `wordcloud_from_frequencies.ipynb` is used to create both the simple wordcloud and the Hanna shaped wordloud. The font size has been reduced to 130 which yields a more even representation of the names.

Both scripts can be found, including additional information, unnder `/code/ichbinxy`


This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
