#!/bin/bash

find data/train -name '*.csv' -exec python3 create_advanced_features.py {} \;
train=80
dev=20
numOfFiles=`find data/train -name '*.features' | wc -l`
let numOfTrainFiles="($train*$numOfFiles)/($train+$dev)"
let numOfDevFiles="($numOfFiles - $numOfTrainFiles)"
cat /dev/null > crf_train.txt
cat /dev/null > crf_dev.txt
processedTrain=0
processedDev=0
find data/train -name '*.features' | while read line; do
	let trainordev=`shuf -i 0-1 -n 1`
	if [ $processedTrain -ge $numOfTrainFiles ]
	then
		let trainordev=1
	fi
	if [ $processedDev -ge $numOfDevFiles ]
	then
		let trainordev=0
	fi
	if [ $trainordev -eq 0 ]
	then
		cat $line >> crf_train.txt
		let "processedTrain++"
	else
		cat $line >> crf_dev.txt
		let "processedDev++"
	fi
done
rm -rf data/train/*.features
