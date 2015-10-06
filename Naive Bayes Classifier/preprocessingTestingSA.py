import sys
from random import randint

output = ""
randomList = ["NEGATIVE","POSITIVE"]
with open(sys.argv[1]) as f:
	for line in f:
		output += randomList[randint(0,1)]+" "
		for word in line.split(" "):
			output += str(int(word.split(":")[0])+1)+":"+word.split(":")[1]+" "
		output = output.rstrip(" ")

with open("test.dat","w+") as f:
	f.write(output)
