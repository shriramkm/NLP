import sys

f1 = open(sys.argv[1])
f2 = open(sys.argv[2],"w+")
outputStr = ""

for line in f1:
	outputStr += line

f2.write(outputStr)
