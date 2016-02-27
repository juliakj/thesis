#!/usr/bin/python
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
    query = argv[0]

    map = getMap()
    top = getTopFrequencies(map)

def getMap():
	path = './map_pickles'
	full = {}
	for filename in os.listdir(path):
		temp = pickle.load(open(path + '/' + filename, 'rb'))
                i = 0
		for specialty in temp:
                    i += 1
                    if specialty not in full:
                        full[specialty] = temp[specialty]
                    else:
                        full[specialty] += " "
                        full[specialty] += temp[specialty]
                    if i == 15:
                        break
	print len(full)
        return full

def getTopFrequencies(map):
    #stopwords = corpus.stopwords.words('english')

    tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
    token_dict = {}
    #for specialty in map:
     #   map[specialty].lower().translate(None, string.punctuation)
    print 'start fit'

    tfs = tfidf.fit_transform(map.values())
    print 'fit done'
    for specialty in map:
        response = tfidf.transform([map[specialty]])
        feature_names = tfidf.get_feature_names()
        print specialty

        featDict = []
        for col in response.nonzero()[1]:
            featDict.append((feature_names[col], response[0,col]))

        print nlargest(20, featDict, key=lambda e:e[1])
        print ''

def sort_matrix(m):
    tuples = izip(m.row, m.col, m.data)
    return sorted(tuples, key=lambda x: (x[2], x[2]))

def tokenize(text):
    tokens = nltk.word_tokenize(text)
#    stems = []
#    for item in tokens:
#        stems.append(PorterStemmer().stem(item))
    return tokens

#        allWords = nltk.tokenize.word_tokenize(map[specialty])
#        allWordDist = nltk.FreqDist(w.lower() for w in allWords)
#        allWordExceptStopDist = nltk.FreqDist(w.lower() for w in allWords if w not in stopwords) 
#        mostCommon= allWordExceptStopDist.most_common(10)


if __name__ == "__main__":
    main(sys.argv[1:])


