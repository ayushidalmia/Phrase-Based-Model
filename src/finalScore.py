'''after obtaining the translationProbability from the alignment matrix,it combines the translation probability from the
language model and returns the findTranslationProbability'''
'''it takes as input the translationProbability as obtained from the word alignments and the unigram probability obtained from
the language model for the source language and returns a final score in the file finalTranslationProbability.txt'''

from collections import defaultdict
import sys

def calculateProbability(translationFile, languageModelFile, outputFileName):

	'''method to combine the translationProbability obtained from languageModel and the alignment file'''
	plm = {}
	f=open(languageModelFile,'r')
	for line in f:
		line = line.strip().split('\t')
		if len(line)==2:
			plm[line[1]] = float(line[0])*-1
	f.close()

	data=[]
	f = open(translationFile, 'r')
	for line in f:
		words = line.strip().split('\t')
		sourceWords = words[1].split(' ')
		value = float(words[2])
		temp = 1
		flag = 0
		for key in sourceWords:
			if key in plm:
				flag = 1
				temp *= plm[key]
		if flag:
			temp = temp * -1
			value += temp
		data.append(words[0]+'\t'+words[1]+'\t'+str(value))
	f.close()

	f=open(outputFileName ,'w')
	f.write('\n'.join(data))
	f.close()


def main():
	if len(sys.argv)!=4:                                                                               #check arguments
		print "Usage :: python finalScore.py translationProbabilityTargetGivenSource.txt trainSource.lm finalTranslationProbabilityTargetGivenSource.txt "
		sys.exit(0)

	calculateProbability(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == "__main__":                                                                              #main
    main()