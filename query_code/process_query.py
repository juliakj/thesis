#!/usr/bin/python
from nltk.stem.porter import PorterStemmer
from heapq import nlargest
import pickle
import sys
import glob
import os
from nltk import corpus
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
import string
import itertools
from operator import itemgetter
from itertools import izip
from scipy.sparse import coo_matrix

def main(argv):
	global path = './map_pickles'
    query = argv[0]

    full = {}
	for filename in os.listdir(path):
    	print filename
    	map = getMap(filename)
    	freqDict = getTopFrequencies(map)
    	full = mergeFreq(full, freqDict)
    print full

def mergeFreq(full, new):
	for specialty in new:
		if specialty not in full:
			full[specialty] = new[specialty]
		else:
			full[specialty] += new[specialty]
	return full

def getMap(filename):
	return pickle.load(open(path + '/' + filename, 'rb'))

def getTopFrequencies(map):
    #stopwords = corpus.stopwords.words('english')

    tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
    tfs = tfidf.fit_transform([ v.lower().translate(None, string.punctuation) for v in map.values()])

    freqDict = {}
    for specialty in map:
        response = tfidf.transform([map[specialty]])
        feature_names = tfidf.get_feature_names()
        # print specialty

        featDict = []
        for col in response.nonzero()[1]:
            featDict.append((feature_names[col], response[0,col]))

        freqDict[specialty] = nlargest(20, featDict, key=lambda e:e[1])

    return freqDict

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    return tokens

if __name__ == "__main__":
    main(sys.argv[1:])
