#!/bin/bash

find data/test -name '*.csv' -exec python3 create_baseline_features.py {} \;
cat /dev/null > crf_test.txt
find data/test -name '*.features' | while read line; do
	cat $line >> crf_test.txt
done
rm -rf data/test/*.features
