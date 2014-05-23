#This module takes as input the bi-text corpuses and the number of sentences.
#It returns the training and testing dataset along with the sentence pairs. 

import random                                        #import libraries
import string
import sys
from collections import defaultdict

def preprocessing(numberOfSentences, sourceFile, targetFile):

    indices=defaultdict(int)
    trainingSource=[]
    trainingTarget=[]
    testingSource=[]
    testingTarget=[]
    
    
    for i in range(numberOfSentences):            #create random numbers                           
        indices[random.randint(0,1920208)] = 1

    with open(sourceFile,'r') as  fSource:        #read from source language corpus
        for index,line in enumerate(fSource):
            if len(line)>0:
                line = line.strip()
                if indices[index] ==1:
                    trainingSource.append(line)   #create training and testing for source language
                else:
                    testingSource.append(line)
                
    with open(targetFile,'r') as  fTarget:         #read from source language corpus
        for index,line in enumerate(fTarget):
            if len(line)>0:
                line = line.strip()
                if indices[index] ==1:
                    trainingTarget.append(line)    #create training and testing for source language
                else:
                    testingTarget.append(line)
    
            
    with open('../Dataset/trainingSource.txt','wb') as f:     #write into training file for source data
        f.write('\n'.join(trainingSource))

    with open('../Dataset/trainingTarget.txt','wb') as f:     #write into training file for target data
        f.write('\n'.join(trainingTarget))

    testingSource=testingSource[:5]                #write into testing file for source data
    with open('../Dataset/testingSource.txt','wb') as f:
        f.write('\n'.join(testingSource))

    testingTarget=testingTarget[:5]                #write into testing file for target data
    with open('../Dataset/testingTarget.txt','wb') as f:
        f.write('\n'.join(testingTarget))

    #return sentencePair

def main():
    if len(sys.argv)!= 4:                                                                               #check arguments
        print "Usage :: python preprocess.py file_source file_target numberOfSentencesForTraining"
        sys.exit(0)
    
    numberOfSentences=int(sys.argv[3])                                                                  #initialisation        
    preprocessing(numberOfSentences, sys.argv[1], sys.argv[2] )


if __name__ == "__main__":                                                                              #main
    main()
