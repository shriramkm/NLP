import sys

outputStr = ""
startLine = 0
finishLine = 0
count = 0
with open("input") as f:
	for line in f:
		count += 1
		if len(sys.argv)==3 and sys.argv[2]=="test":
			if line=="TEST\n":
				startLine = count-1
		else:
			if line=="DEV\n":
                                startLine = count
			if line=="TEST\n":
				break
finishLine = count
print(str(startLine)+" "+str(finishLine))
		
count = 0
with open(sys.argv[1]) as f:
	for line in f:
		count+=1
		if count>=startLine and count<=finishLine:
			if int(line.split("\t")[0])==1:
				outputStr+="SPAM\n"
			if int(line.split("\t")[0])==0:
				outputStr+="HAM\n"

#print(str(startLine)+" "+str(finishLine))
with open("output","w+") as f1:
	f1.write(outputStr)
