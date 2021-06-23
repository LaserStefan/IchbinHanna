# Script for language codes frequencies

Authors: Jana Lasser, Stefan Laser, Migle Bareikyte, Maria Blöchl, Tim Schatto-Eckrodt, Elen Le Foll, Christian Funk, David Adler

[![CC BY 4.0][cc-by-shield]][cc-by]

[This script is part of the „Analysis of Tweets for the #IchBinHannah Campaign“ project. For more details and licence see: https://github.com/LaserSteff/-IchbinHanna/blob/main/README.md]

The script collects language codes from jsonl.xz files or foldes containing multiple such files. Its returns a .csv file with absolute and relative frequencies and saves it within a subfolder „lf_results" of the folder you run the script in. The files are automatically decompressed. Retweets are exclude from the frequency count.

### Usage

Navigate to the folder with the script.

```python3 language_tweets.py [ARGUMENTS] PATH```

ARGUMENTS: 

`file` if you want to analyse a single file

`folder` if you want to analyse a 

`--help` for basic information

PATH: either (relative or absolute) path to file or to folder

### Todos
Sorting csv lines by frequency




This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
