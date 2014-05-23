'''-t'''
''' it takes as input the word alignment of both the languages and returns a file called phrases.txt which contains
all the consistent phrases'''

import sys                                                                                             #import libraries
from alignment import findAlignment



def checkConsistency(fstart, fend, estart, eend, wordAlignment, english, german):

	'''function to check whether the phrase is consistent or not'''
	flag =1

	listEnglish =[]
	listGerman = []

	for i in range(len(english)):
		if i >= estart and i<=eend:
			listEnglish.append(i)

	for i in range(len(german)):
		if i >= fstart and i <=fend:
			listGerman.append(i)

	for e in listEnglish:
		for f in range(len(german)):
			if wordAlignment[e][f]==1:
				if f >= fstart and f <=fend:
					continue
				else:
					flag = 0

	for f in listGerman:
		for e in range(len(english)):
			if wordAlignment[e][f]==1:
				if e >= estart and e <=eend:
					continue
				else:
					flag = 0

	return flag


def findPhrase(fstart, fend, estart, eend, english, german):

	'''given the starting and end points, it returns the phrase for both the source and the target language'''
	phraseE = []
	#print fstart, fend, estart, eend
	for i in range(estart,eend+1):
		phraseE.append(english[i])

	phraseG = []
	for i in range(fstart,fend+1):
		phraseG.append(german[i])

	return [' '.join(phraseE), ' '.join(phraseG)]

def extract(fstart, fend, estart, eend, wordAlignment, english, german):
	'''this method extracts the consistent phrases and returns it to the extractPhrases method'''
	if fend == -1:
		return 'NULL'

	else:
		flag=checkConsistency(fstart, fend, estart, eend, wordAlignment, english, german)
		if flag:
			return findPhrase(fstart, fend, estart, eend, english, german)
		else:
			return 'NULL'

def extractPhrases(englishToGerman, germanToEnglish):
	'''this method reads the file for both the source and target language and returns the phrases extracted from the
	sentences. The phrases are consistent in nature'''

	data=[]
	feg = open(englishToGerman, 'r')
	fge = open(germanToEnglish,'r')
	count = 0
	while True:
		count+=1
		print count
		line = feg.readline()
		if line == "":
			break
		englishToGerman1 = feg.readline()
		englishToGerman2 = feg.readline()
		#print englishToGerman1
		line = fge.readline()
		germanToEnglish1 = fge.readline()
		germanToEnglish2 = fge.readline()
		#print germanToEnglish1

		wordAlignment, english, german = findAlignment(englishToGerman1, englishToGerman2, germanToEnglish1, germanToEnglish2)

		lEnglish = len(english)
		lGerman = len(german)
		
		phrases = []
		for estart in range(lEnglish):
			for eend in range(estart,(lEnglish)):
				fstart = lGerman
				fend = -1
				for i in wordAlignment:
					if i <= eend and i >= estart:
						for j in wordAlignment[i]:
							fstart = min(j, fstart)
							fend = max(j, fend)
				if ((eend - estart) <= 20) or ((fend -fstart) <= 20) :
					phrases.append([estart, eend, fstart, fend])
		#print phrases
		for key in phrases:
			estart = key[0]
			eend = key[1]
			fstart = key [2]
			fend = key[3]
			phrase = extract (fstart, fend,estart, eend,wordAlignment, english, german)
			if phrase!= 'NULL':
				#print phrase
				data.append(phrase[0]+'\t'+phrase[1])
	feg.close()
	fge.close()

	f=open('phrases.txt','w')
	f.write('\n'.join(data))
	f.close()
	
def main():
	if len(sys.argv)!=3:                                                                               #check arguments
		print "Usage :: python phraseExtraction.py englishToGerman germanToEnglish"
		sys.exit(0)

	extractPhrases(sys.argv[1], sys.argv[2])

if __name__ == "__main__":                                                                              #main
    main()
