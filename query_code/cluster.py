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
import process_query
import MySQLdb
import matplotlib
matplotlib.use('Agg')
import networkx as nx


def main():
    npis = getData()
    print len(npis)
    print len(set(npis))


def getData():
    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                         user="root",         # your username
                         passwd="Galdorhavens0!",  # your password
                         db="db")        # name of the data base
    cur = db.cursor()

    cur.execute("SELECT npi FROM violations")

    return cur.fetchall()
        
    

if __name__ == "__main__":
    main()
