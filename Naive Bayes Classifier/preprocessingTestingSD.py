import sys,os,glob
from random import randint

def readFiles(directoryPath):
	global vocabDict
	dictStr = ""
	pwd = os.getcwd()
	os.chdir(directoryPath)
	randomList = ["HAM","SPAM"]
	for file in glob.glob("*.txt"):
		fileDict = {} 
		currentFile = open(os.path.abspath(file), "r", encoding="latin1")
		for content in currentFile:
			content = content[:-1]
			splitContent = content.split()
			for token in splitContent:
				if token in vocabDict:
					if vocabDict[token] in fileDict:
						fileDict[vocabDict[token]] += 1
					else:
						fileDict[vocabDict[token]] = 1
		label = randomList[randint(0,1)]
		dictStr += label+" "
		fileDict = (sorted(fileDict.items())) 
		for key,val in fileDict:
			dictStr += str(key) + ":" + str(val) + " "
		dictStr += "\n"
	os.chdir(pwd)
	return dictStr

vocabFile = "/media/shriram/Additional/nlp/Assignment 2/data/enron.vocab"
vocabDict = {}
vocabSize = 0
dictStr = ""
with open(vocabFile, "r", encoding="latin1") as f:
        for line in f:
                vocabSize += 1
                vocabDict[line[:-1]] = vocabSize;
dictStr += readFiles("spam_or_ham_test");

with open("test.dat","w+") as f:
	f.write(dictStr)
