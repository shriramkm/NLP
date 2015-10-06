import sys

outputStr = ""
with open(sys.argv[1]) as f:
	for line in f:
		if float(line)>0:
			outputStr+="SPAM\n"
		else:
			outputStr+="HAM\n"

with open("output","w+") as f1:
	f1.write(outputStr)
