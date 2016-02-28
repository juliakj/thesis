#!/usr/bin/python
from nltk.stem.porter import PorterStemmer
from difflib import SequenceMatcher
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
from nltk.stem import *


def main(argv):
    query = argv[0]
    results = process(query)
    for r in results:
        print r

def process(query):
    
    types = []

    map = pickle.load(open('fullMap.p', 'rb'))
    types = getSpecialties(map, query)
    return sorted(types.items(), key=itemgetter(1), reverse=True)
        

def getSpecialties(map, query):
    types = {}
    stemmer = SnowballStemmer("english")

    for spec in map:
        for q in query.split():
            if isMatch(spec.lower(), q.lower()):
#                print 'type match ' + spec
                types[spec] = 1
        for feat in map[spec]:
            for q in query.split():
                if isMatch(feat[0].lower(), q.lower()):
                    if spec not in types:
                        types[spec] = feat[1]
                    else:
                        types[spec] += feat[1]
    return types

def isMatch(s, query):
    stemmer = SnowballStemmer("english")
    l = [stemmer.stem(w) for w in s.split()]
    q = stemmer.stem(query)
    if s.find(q) != -1 or string.join(l).find(q) != -1 or isSimilar(q, s):
        return True
    if s.find(query) != -1 or string.join(l).find(query) != -1 or isSimilar(query, s):
        return True
    for w in s.split():
        if isSimilar(w, query) or isSimilar(w, q):
            return True
    return False

def isSimilar(a, b):
    return SequenceMatcher(None, a, b).ratio() > 0.75    

if __name__ == "__main__":
    main(sys.argv[1:])
