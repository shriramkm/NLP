import sys
from random import randint

outputStr = ""
for i in [1,2]:
	with open(sys.argv[i]) as f:
		contents = f.read()
		contents = contents.replace("SPAM","1")
		contents = contents.replace("HAM","0")
	if i==1:
		outputStr += contents+"DEV\n"
	if i==2:
		outputStr += contents+"TEST\n"
if len(sys.argv)==5:
	with open(sys.argv[4]) as f1:
		for line in f1:
			outputStr += line
	outputStr = outputStr.replace("SPAM","1")
	outputStr = outputStr.replace("HAM","0")
else:
	outputStr = outputStr[:outputStr.rfind("TEST\n")]
with open(sys.argv[3],"w+") as f:
	outputStr = outputStr.replace(":"," ")
	f.write(outputStr)
