'''given a pair of sentences along with the word alignment this code returns the union of the word alignment matrix'''
'''it serves as a helper function to phraseExtraction Algorithm'''

from collections import defaultdict
import string

def findAlignment(german, englishAligned, english, germanAligned):
	
	wordAlignment = defaultdict(lambda: defaultdict(int))				
	wordIndexEnglish = defaultdict(lambda: -1)
	wordIndexGerman = defaultdict(lambda: -1)

	german  = german.strip().split()
	for i in range(len(german)):
		german[i] = german[i].translate(string.maketrans("",""), string.punctuation)
		
		
	english = english.strip().split()
	for i in range(len(english)):
		english[i] = english[i].translate(string.maketrans("",""), string.punctuation)


	englishAligned = englishAligned.strip().split(" })")
	englishAligned = englishAligned[1:]
	count = 0
	for key in englishAligned:
		words = key.split('({')
		if len(words)>1 and words[1]!='':
			englishWord = words[0].strip()
			englishWord = englishWord.translate(string.maketrans("",""), string.punctuation)
			indices = words[1].split()
			for i in indices:
				i = int(i)
				wordAlignment[count][i-1] = 1
		count += 1
				
	germanAligned = germanAligned.strip().split(" })")
	germanAligned = germanAligned[1:]
	count = 0
	for key in germanAligned:
		words = key.split('({')
		if len(words)>1 and words[1]!='':
			germanWord = words[0].strip()
			germanWord = germanWord.translate(string.maketrans("",""), string.punctuation)
			indices = words[1].split()
			for i in indices:
				i= int(i)
				wordAlignment[i-1][count] = 1			
		count +=1

	return wordAlignment, english, german