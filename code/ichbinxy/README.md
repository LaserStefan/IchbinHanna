# Script for names in "ich bin [NAME]" formula

Authors: Jana Lasser, Stefan Laser, Migle Bareikyte, Maria Blöchl, Tim Schatto-Eckrodt, Elen Le Foll, Christian Funk, David Adler

[![CC BY 4.0][cc-by-shield]][cc-by]

This script is part of the „Analysis of Tweets for the #IchBinHannah Campaign“ project. For more details and licence see: https://github.com/LaserSteff/-IchbinHanna/blob/main/README.md

## Getting the names: python script `ichbinxy.py`

The script collects the names given within the "ich bin [NAME]" formula within tweet texts from .jsonl.xz files based on the output data of the twitter API v2 collected with twarc2. The names are written in two .csv files in a subdirectory /results:

* one with a simple listing of all the names for every time they occure.
* one as a list of name and frequency of the occurence.

Retweets are automatically excluded from the collection.
Special characters and numbers are automatically substituted by " " before further collecting data from the text.

For filtering out non-names the `not_names_stopwords.txt` list from the subdirectory /resources is used. New word can be added by simply adding a new line with an additional stopword.

### Usage

Navigate to the folder with the script. If wanted, place the .jsonl.xz file in the same folder. Make sure the file not_names_stopwords.txt exists in subfolder resources.

`python3 ichbinxy.py PATH`

PATH: either (relative or absolute) path to file or to folder

The files `names.csv` and `names_freq.csv`are written into the subdirectory /results.

### Version
1.0 (28.6.2021)

### To Do

* Sorting csv lines by frequency. Till now frequencies are not sorted from high to low.
* It would be nice if the script for creating wordclouds could directly get the dictionaries from ichbinxy.py without taking the detour of the .csv file.


## Producing the wordclouds: jupyter notebook `wordcloud_from_frequencies.ipynb`

The jupyter notebook `wordcloud_from_frequencies.ipynb` uses the `names_freq.csv` file produced by the `ichbinxy.py` skript in order to create two wordclouds.

1. A simple wordcloud.
2. A wordcloud in the shape of Hannas contour (Hanna being the animated figure from the educational video that sparked the #IchBinHanna campaign). This second wordcloud requires the file Hanna.jpg from the subdirectory /resources. The corresponding image can also be found here:
https://github.com/LaserSteff/-IchbinHanna/tree/main/resources/images/Hanna.

Note that the maximal font size is set to 130 when producing the wordcloud. This creates a more even distribution of the names. But it is potentially not desired when you want to use the wordcloud to make stronger claims on the frequency of certain names.

### Usage

The script should be placed in the same directory as the `ichbinxy.py` script as it uses the subdirectory /results created by `ichbinxy.py` to collect the data for the wordcloud.

The resulting wordlouds are written in this same directory.

### To Do
* The wordclouds size and dpi should be optimized. It seems not to adequatly react to a manipulation of the corresponding arguments from the Wordcloud package.

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
