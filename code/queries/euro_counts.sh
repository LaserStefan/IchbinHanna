#!/bin/bash
twarc2 counts --start-time 2021-01-01 --end-time 2021-06-27 --archive --granularity day --csv '(#euro2020 OR #EURO2020 OR #Euro2020 OR #euro OR #EURO) lang:de' > ../../data/counts/euro_counts.csv
