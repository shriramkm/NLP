import sys;

with open(str(sys.argv[1]),'r') as inputFile:
	content = inputFile.readlines()
outputFile = open(str(sys.argv[2]),'w+')
for sentence in content:
	outputFile.write(str(len(sentence.split()))+"\n")
