import sys

f = open(sys.argv[1])
processedStr = ""

for line in f:
	line = line[:-1].rstrip()
	words = line.split(" ")
	rating = int(words[0])
	if rating<5:
		processedStr += "NEGATIVE "
	if rating>6:
		processedStr += "POSITIVE "
	for i in range(1,len(words)):
		processedStr += str(int(words[i].split(":")[0])+1)+":"+words[i].split(":")[1]+" "
	processedStr = processedStr.rstrip()
	processedStr += "\n"

f= open(sys.argv[2],"w+")
f.write(processedStr)		
