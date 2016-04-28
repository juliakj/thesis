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
import operator
import MySQLdb
import networkx as nx
import matplotlib.pyplot as plt


def get(argv):
    sorted_p = getDegree()
    i = 0 
    
    d = [i[1][0] for i in sorted_p]
    print len(d)

    plt.hist(d, 75)

    plt.xlabel('Number of referral neighbors')
    plt.ylabel('Frequency')
    plt.title('Distribution of Referral Neighbors accross Providers')

    plt.show()

def getDegree():
#    print providers
    data = pickle.load(open('/home/ubuntu/mygit/query_code/fullNetMap.p', 'rb'))
    print len(data)
    print data.items()[0]
    sorted_x = sorted(data.items(), key=lambda x:x[1][0])

#    sorted_x = sorted(data.items(), key=operator.itemgetter(1)[0])
    return sorted_x



if __name__ == "__main__":
    get(sys.argv[1:])
