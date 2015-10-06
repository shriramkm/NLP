import sys

outputStr = ""
with open(sys.argv[1]) as f:
	for line in f:
		if float(line)>0:
			outputStr+="POSITIVE\n"
		else:
			outputStr+="NEGATIVE\n"

with open("output","w+") as f1:
	f1.write(outputStr)
