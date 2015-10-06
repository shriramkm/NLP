import sys,random

trainingFileSize = 100
devFileSize = 100
data = {}
with open(sys.argv[1]) as f: #Open original input file
	count = 0
	for line in f:
		data[count] = line
		count+=1
	noOfTrainingData = (trainingFileSize*count/(100))
	noOfDevData = (devFileSize*count/(100))
	randomListTraining = []
	randomListDev = []
	trainingStr = ""
	devStr = ""
	if trainingFileSize+devFileSize <= 100:
		randomListTraining = random.sample(range(0,count),int(noOfTrainingData))
		currentCount = 0
		for i in range(0,count):
			if currentCount==noOfDevData:
				break
			if i not in randomListTraining:
				randomListDev.append(i)
	else:
		randomListTraining = random.sample(range(0,count),int(noOfTrainingData))
		randomListDev = random.sample(range(0,count),int(noOfDevData))
	for i in range(0,count):
		if i in randomListTraining:
			trainingStr += data[i]
		if i in randomListDev:
			devStr += data[i]
	trainingFile = open(sys.argv[2],"w+")		#Open Training file
	trainingFile.write(trainingStr)
	devFile = open(sys.argv[3],"w+")		#Open Development file
	devFile.write(devStr)
