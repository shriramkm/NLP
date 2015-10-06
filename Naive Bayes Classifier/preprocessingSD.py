import sys,glob,os

#Function that reads all the txt files inside the directory Path
#and tokenizes each file to calculate the frequency of each token.
#These frequencies are stored in a common Program Data format as
#follows(There's one such row as given below for each txt file)
#LABEL FEATURE1:VALUE1 FEATURE2:VALUE2 ...
def readFiles(directoryPath,label):
	global vocabDict
	dictStr = ""
	pwd = os.getcwd()
	os.chdir(directoryPath)
	for file in glob.glob("*.txt"):
		#print(str(os.path.abspath(file)))
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
dictStr += readFiles("./enron1/ham","HAM");
dictStr += readFiles("./enron1/spam","SPAM");
dictStr += readFiles("./enron2/ham","HAM");
dictStr += readFiles("./enron2/spam","SPAM");
dictStr += readFiles("./enron4/ham","HAM");
dictStr += readFiles("./enron4/spam","SPAM");
dictStr += readFiles("./enron5/ham","HAM");
dictStr += readFiles("./enron5/spam","SPAM");
#print(dictStr.count("\n"))
programDataFile = open(sys.argv[1],"w+")
programDataFile.write(dictStr)
