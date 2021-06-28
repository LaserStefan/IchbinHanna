#!/bin/bash
twarc2 search --start-time 2021-01-01 --end-time 2021-06-27 --archive '(#ESC OR #EuroVision2021 OR #esc OR #Esc OR #eurovision2021 OR #Eurovision2021 OR #euroVision2021) lang:de' > ../../data/ESC.jsonl

