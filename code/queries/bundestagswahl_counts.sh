#!/bin/bash
twarc2 counts --start-time 2021-01-01 --end-time 2021-06-30 --archive --granularity day --csv '(#Bundestagswahl2021 OR #bundestagswahl2021 OR #BUNDESTAGSWAHL2021 OR #BundesTagsWahl2021 OR #BTW2021 OR #btw2021 OR #btw21 OR #BTW21 OR #Bundestagswahl21 OR #bundestagswahl21 OR #BUNDESTAGSWAHL21) lang:de' > ../../data/counts/bundestagswahl_counts.csv
