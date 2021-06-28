#!/bin/bash
twarc2 search --start-time 2021-01-01 --end-time 2021-06-27 --archive '(#euro2020 OR #EURO2020 OR #Euro2020 OR #euro OR #EURO)  lang:de' > ../../data/tweets/euro.jsonl

