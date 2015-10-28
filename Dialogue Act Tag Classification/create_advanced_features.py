from hw3_corpus_tool import get_utterances_from_file
from hw3_corpus_tool import get_utterances_from_filename
import sys, re, string

def main(currentFile):
	featureStr = ""
	dialogUtterances = get_utterances_from_filename(currentFile)
	prevSpeaker = ""
	for dialogUtterance in dialogUtterances:
		dialogActTag = dialogUtterance.act_tag
		if dialogActTag is None:
			dialogActTag = "UNK"
		currentSpeaker = dialogUtterance.speaker
		if dialogUtterance.pos is not None:
			tokens = [word.token for word in dialogUtterance.pos]
			poss = [word.pos for word in dialogUtterance.pos]
		featureStr += dialogActTag+"\t"
		if prevSpeaker=="":
			featureStr += "FirstUtterance="+dialogUtterance.text+"\t"
		if prevSpeaker != "":
			if(prevSpeaker != currentSpeaker):
				featureStr += "SpeakerChanged=Yes\t"
			else:
				featureStr += "SpeakerChanged=No\t"
		if(dialogUtterance.pos is None or tokens is None):
			featureStr += "Text="+dialogUtterance.text+"\t" 
		elif(len(tokens)==1 and len(poss)==1):
			if((tokens[0]=="." and  poss[0]==".") or (tokens[0] is None)):
				featureStr += "Text="+dialogUtterance.text+"\t" 
		else:
			for i in range(0,len(tokens)):
				if tokens[i]=="MUMBLEx":
					featureStr += "Text="+dialogUtterance.text+"\t"
				else:
					featureStr +="Unigram="+tokens[i]+"\t"+"Unigram POS="+poss[i]+"\t"
			for i in range(0,len(tokens)-1):
				if tokens[i]=="MUMBLEx":
					featureStr += "Text="+dialogUtterance.text+"\t"
				else:
					featureStr +="Bigram="+tokens[i]+"|"+tokens[i+1]+"\t"+"Bigram POS="+poss[i]+"|"+poss[i+1]+"\t"
			for i in range(0,len(tokens)-2):
				if tokens[i]=="MUMBLEx":
					featureStr += "Text="+dialogUtterance.text+"\t"
				else:
					featureStr +="Trigram="+tokens[i]+"|"+tokens[i+1]+"|"+tokens[i+2]+"\t"+"Trigram POS="+poss[i]+"|"+poss[i+1]+"|"+poss[i+2]+"\t"
			pattern = re.compile('[\W_]$')
			words = pattern.sub('', dialogUtterance.text)
			for word in words.split():
				if word!="":
					featureStr += "Transcript="+word+"\t"
		featureStr = featureStr.strip()
		featureStr += "\n"
		prevSpeaker = currentSpeaker
	featureStr.replace(":","{colon}")
	featureStr.replace("\\","{backslash}")
	featureStr = featureStr.strip()
	featureStr += "\n\n"
	f = open(currentFile+".features","w+")
	f.write(featureStr)
if __name__=='__main__':
	sys.exit(main(sys.argv[1]))
