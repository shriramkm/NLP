import sys

output = {}
testingData = {}
classified = {}
correctlyClassified = {}
belongsToClass = {}

f = open(sys.argv[1])	#open output
output = f.read().split("\n")

f1 = open(sys.argv[2])	#open testing file	
#searchfile = open(sys.argv[3], "r")     #open preprocessed data
i=0
for line in f1:
	match = line.split(" ")[0]
	line = line[line.find(" ")+1:].rstrip()
	#print(str(i)+" MATCH : "+match)
	if match not in belongsToClass:
		belongsToClass[match] = 1
	else:
		belongsToClass[match] += 1
	#print("..."+match+"..."+output[i]+"...")
	if match==output[i]:
		if match not in correctlyClassified:
			correctlyClassified[match] = 1
		else:
			correctlyClassified[match] += 1	
	if output[i] not in classified:
		classified[output[i]] = 1
	else:
		classified[output[i]] += 1
	i+=1
totalCorrectlyClassified = 0
for label in classified:
	totalCorrectlyClassified += correctlyClassified[label]
	precision = float(correctlyClassified[label]/classified[label])
	recall = float(correctlyClassified[label]/belongsToClass[label])
	print("Precision of "+label+" : "+str(precision))
	print("Recall of "+label+" : "+str(recall))
	print("F-Score of "+label+" : "+str(float((2*precision*recall)/(precision+recall))))
	print("CC : "+str(correctlyClassified[label]))
	print("BT : "+str(belongsToClass[label]))
	print("CL : "+str(classified[label]))
testingFile = open(sys.argv[2])
accuracy = totalCorrectlyClassified/len(testingFile.read().split("\n"))
print("Accuracy : "+str(accuracy))
