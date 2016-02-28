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
import process_query

def main(argv):
    query = argv[0]
    results = process_query.process(query)
    for r in results:
        print r


if __name__ == "__main__":
    main(sys.argv[1:])
