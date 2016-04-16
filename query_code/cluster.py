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



def getData(i):
    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                         user="root",         # your username
                         passwd="Galdorhavens0!",  # your password
                         db="db")        # name of the data base
    cur = db.cursor()
    if i == 0:
        offset = ''
    else:
        offset = str(i) + ', '
    cur.execute("SELECT * FROM referrals limit " + offset + "500000")

    return cur.fetchall()
        
    

if __name__ == "__main__":
    main()
