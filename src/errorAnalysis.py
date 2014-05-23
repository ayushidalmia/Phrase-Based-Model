'''this method takes as input the translation, actual input and the real output and gives a precision and recall value for each sentence'''

import sys

def calculatePrecision(translation, actual):
	'''calculate precision'''
	count = 0
	for key in translation:
		if key in actual:
			count+=1
	return float(count)/len(translation)

def calculateRecall(translation, actual):
	'''calculate recall'''
	count = 0
	for key in actual:
		if key in translation:
			count+=1
	return float(count)/len(actual)


def main():
	if len(sys.argv)!=2:                                                                               #check arguments
		print "Usage :: python errorAnalysis.py translationEnglishToGermanTraining.txt "
		sys.exit(0)

	data = []
	data.append(sys.argv[1])
	f=open(sys.argv[1],'r')
	for line in f:
		translation = f.next().strip().split(' ')
		actual = f.next().strip().split(' ')
		precision = calculatePrecision(translation, actual)
		recall = calculateRecall(translation,actual)
		data.append(str(precision)+'\t'+str(recall))
	f.close()

	f=open('evaluation.txt','a')
	f.write('\n'.join(data))
	f.write('\n')
	f.close()

if __name__ == "__main__":                                                                              #main
    main()