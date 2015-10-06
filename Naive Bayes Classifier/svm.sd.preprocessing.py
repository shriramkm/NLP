import sys

with open(sys.argv[1]) as f:
	contents = f.read()
	contents = contents.replace("SPAM","1")
	contents = contents.replace("HAM","-1")
with open(sys.argv[1],"w+") as f1:
	f1.write(contents)
