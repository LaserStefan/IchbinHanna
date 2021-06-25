# Scripts for ratios of tweet types

Authors: Jana Lasser, Stefan Laser, Migle Bareikyte, Maria Blöchl, Tim Schatto-Eckrodt, Elen Le Foll, Christian Funk, David Adler

[![CC BY 4.0][cc-by-shield]][cc-by]

[This script is part of the „Analysis of Tweets for the #IchBinHannah Campaign“ project. For more details and licence see: https://github.com/LaserSteff/-IchbinHanna/blob/main/README.md

## Script tweet_types_compared.ipynb

The script uses the tweet_ratios_rel function from the ratio of retweet script to compare the distribution between two collections of tweets. It is now based on the comparison of #95vsWissZeitVG and #IchBinHanna, but can easily adapted for comparing other files. The script produces a diagram of stacked bars like this: 

![plot](https://github.com/LaserSteff/-IchbinHanna/blob/main/plots/tweet_types_compared.png)

## Script ratio of retweets in corpus

Returns total number of tweets, number of retweets, number of quotes, number of replies and number of new tweets + correspodning ratios compared to the number of all tweets for any twarc2 generated .json.xz file in shell.

**Example for results**

```
Absolute values
path: IchBinHanna.jsonl.xz
all_tweets: 27334
retweets: 21673
quotes: 1222
replies: 1318
new_tweets: 3121


Relative values
path: IchBinHanna.jsonl.xz
abolute_tweets: 27334
retweets: 79.28952952367015
quotes: 4.4706226677398115
replies: 4.821833613814297
new_tweets: 11.418014194775736
```


### Usage

**Stand alone script**

Navigate to the folder with the script.

```python3 retweet_ratio.py PATH```

**Call function from script**

You can use two functions from the script to get the abolute or relative distribution of types of tweets.

For absolute values use `get_freq`, for relative values `get_rel_freq`. You can import these functions by positioning the script retweet_ratio.py script in your script’s folder and calling it with.

```from retweet_ratio import tweet_ratios_abs```

or

```from retweet_ratio import tweet_ratios_rel```

Then call the function get_freq, passing the path of the file you want to get the ratios for. For instance: 
`get_freq(IchBinHanna.jsonl.xz)`
if this file is situated in the same folder as retweet_ratio.py

The functions returne a dictionary with the following structure:

```
{
    'path': 'IchBinHanna.jsonl.xz', 
    'all_tweets': 27334, 
    'retweets': 21673, 
    'quotes': 1222, 
    'replies': 1318, 
    'new_tweets': 3121

}
```

or

```
{
    'path': 'IchBinHanna.jsonl.xz', 
    'abolute_tweets': 27334, 
    'retweets': 79.28952952367015, 
    'quotes': 4.4706226677398115, 
    'replies': 4.821833613814297, 
    'new_tweets': 11.418014194775736}
```


This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
