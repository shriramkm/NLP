import sys,math,operator,pdb

modelFile = sys.argv[1]		#Model File
testingFile = sys.argv[2]	#Development File
probabilityDict = {}
classProbability = {}
countDict = {}

with open(modelFile) as f:
	for line in f:
		line = line[:-1].rstrip()
		splitLine = line.split(" ")
		if splitLine[0] not in probabilityDict:
			probabilityDict[splitLine[0]] = {}
		if len(splitLine)==2:
			classProbability[splitLine[0]] = splitLine[1]	
		else:
			probabilityDict[splitLine[0]][splitLine[1]] = splitLine[2]
outputStr = ""
i = 0
with open(testingFile) as f:
	for line in f:
		line = line[line.find(" ")+1:]
		line = line[:-1].rstrip()
		i += 1
		splitLine = line.split(" ")
		prob = {}
		for label in probabilityDict:
			prob[label] = math.log10(float(classProbability[label]))
		for label in probabilityDict:
			for word in splitLine:
				token = word.split(":")[0]
				frequency = word.split(":")[1]
				if token in probabilityDict[label]:
					prob[label] += (int(frequency)*(math.log10(float(probabilityDict[label][token]))))
		maxLabel = max(prob, key=prob.get)
		outputStr += maxLabel+"\n"

outputFile = open("output","w+")
outputFile.write(outputStr)
