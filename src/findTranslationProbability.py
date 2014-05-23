'''after obtaining the consistent phrases from the phrase extraction algorithm we next move to find the translationProbability
this is done by calculating the relative occurrences of the target phrase for a given source phrase for both directions'''
'''it takes as input the phrases.txt file and returns the translationProbability in the file named 
translationProbabilityGermanGivenEnglish.txt and translationProbabilityEnglishGivenGerman.txt'''

from collections import defaultdict
import sys
import math

countGerman=defaultdict(lambda: defaultdict(int))
sumCountEnglish=defaultdict(int)
countEnglish = defaultdict(lambda: defaultdict(int))
sumCountGerman = defaultdict(int)


def findTranslationProbability(phrasesFile):

	f = open (phrasesFile, 'r')
	for line in f:
		phrases = line.strip().split('\t')
		if len(phrases) == 2:
			countGerman[phrases[0]][phrases[1]]+=1
			sumCountEnglish[phrases[0]]+=1
			countEnglish[phrases[1]][phrases[0]]+=1
			sumCountGerman[phrases[1]]+=1
	f.close

	data=[]
	for key in countGerman:
		for key1 in countGerman[key]:
			translationProbability = math.log(float(countGerman[key][key1])/sumCountEnglish[key])
			data.append(key1+'\t'+key +'\t'+str(translationProbability))

	f=open('translationProbabilityTargetGivenSource.txt','w')
	f.write('\n'.join(data))
	f.close()

	data=[]
	for key in countEnglish:
		for key1 in countEnglish[key]:
			translationProbability = math.log(float(countEnglish[key][key1])/sumCountGerman[key])
			data.append(key1+'\t'+key+'\t'+str(translationProbability))

	f=open('translationProbabilitySourceGivenTarget.txt','w')
	f.write('\n'.join(data))
	f.close()

def main():
	if len(sys.argv)!=2:                                                                               #check arguments
		print "Usage :: python findTranslationProbability phrases.txt"
		sys.exit(0)

	findTranslationProbability(sys.argv[1])

if __name__ == "__main__":                                                                              #main
    main()
