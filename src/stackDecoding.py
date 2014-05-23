'''this function gives the translation for a given sentence based on hypothesis recombiniation.'''
'''it takes as input the finalTranslationProbability and the input file and returns the output translation in translation.txt'''

import sys
from collections import defaultdict
import operator
import string

def findBestTranslation(finalTranslationProbability, inputFile):

	tp = defaultdict(dict)
	f=open(finalTranslationProbability,'r')
	for line in f:
		line = line.strip().split('\t')
		line[0] = line[0].translate(string.maketrans("",""), string.punctuation)
		line[1] = line[1].translate(string.maketrans("",""), string.punctuation)
		tp[line[0]][line[1]] = float(line[2])
	f.close()

	
	
	data=[]
	f=open(inputFile,'r')
	for line in f:
		translationScore = defaultdict(int)
		translationSentence = defaultdict(list)
		words = line.strip().split(' ')
		for i in range(len(words)):
			words[i] = words[i].translate(string.maketrans("",""), string.punctuation)
		count = 1
		for i in range(len(words)):
			translation = ''
			for j in range(len(words)-count+1):
				phrase = words[j:j+count]
				phrase = ' '.join(phrase)
				#print phrase
				if phrase in tp:
					translationPhrase = max(tp[phrase].iteritems(), key=operator.itemgetter(1))[0]
					translationScore[count]+=tp[phrase][translationPhrase]
					translation+=translationPhrase+' '
			if translation!='':
				translationSentence[count].append(translation)
			count+=1
		index = max(translationScore.iteritems(), key=operator.itemgetter(1))[0]
		finalTranslation = ' '.join(translationSentence[index])
		data.append(finalTranslation)

	f=open('translation.txt','w')
	f.write('\n'.join(data))
	f.close()

def main():
	if len(sys.argv)!=3:                                                                               #check arguments
		print "Usage :: python finalScore.py finalTranslationProbability.txt inputFile.txt "
		sys.exit(0)

	findBestTranslation(sys.argv[1], sys.argv[2])

if __name__ == "__main__":                                                                              #main
    main()