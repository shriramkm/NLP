import sys

countDict = {}
PofWordGivenClass = {}
PofClass = {}
totalExamples = 0
trainingStr = ""
vocabDict = {}

with open(sys.argv[1]) as f:	#Open training file
	totalWordCount = {}
	for line in f:
		line = (line[:-1]).rstrip()
		totalExamples += 1
		tokens = line.split(" ")
		label = tokens[0]
		if label not in totalWordCount:
			totalWordCount[label] = 0
		if label not in PofClass:
                        PofClass[label] = 0
		if label not in countDict:
			countDict[label] = {}
		for i in range(1,len(tokens)):
			token = tokens[i].split(":")[0]
			frequency = int(tokens[i].split(":")[1])
			if token in countDict[label]:
				countDict[label][token] += frequency
			else:
				countDict[label][token] = frequency
				vocabDict[token] = 1
			totalWordCount[label] += frequency
		PofClass[label] += 1
	#print(totalWordCount)
	for label in PofClass:
		trainingStr += label+" "+str(float(PofClass[label]/totalExamples))+"\n"

	for word in vocabDict:
                for label in countDict:
                        if word not in countDict[label]:
                                countDict[label][word] = 0
	
	for label in countDict:
		if label not in PofWordGivenClass:
			PofWordGivenClass[label] = {}
		for word in countDict[label]:
			PofWordGivenClass[label][word] = float((int(countDict[label][word])+1)/((totalWordCount[label])+len(vocabDict)))
			trainingStr += label+" "+word+" "+str(PofWordGivenClass[label][word])+"\n"

modelFile = open(sys.argv[2],"w+")	#Open model file
modelFile.write(trainingStr)
