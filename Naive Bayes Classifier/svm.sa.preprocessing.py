import sys

with open(sys.argv[1]) as f:
	contents = f.read()
	contents = contents.replace("POSITIVE","1")
	contents = contents.replace("NEGATIVE","-1")
with open(sys.argv[1],"w+") as f1:
	f1.write(contents)
