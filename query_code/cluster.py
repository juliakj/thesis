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
    '''
    violations = getViolationData()
    print len(violations)
    print len(set(violations))

    providers = getallNpis()
    print len(providers)

    d = dict((el[0],[1 if el[0] in violations else 0, 0]) for el in providers)
    '''
    d = pickle.load(open("currentQuality.p", "rb"))
   
    services = getServiceData()
#    del providers
    print "got services"
    for s in services:
        d[s[0]][1] += s[1]

    print d[1003000126]

    pickle.dump(d, open("currentQuality.p", "wb"))

def getServiceData():
    db = MySQLdb.connect(host="localhost",    # your host, usually localhost                                                                                               
                         user="root",         # your username                                                                                                               
                         passwd="Galdorhavens0!",  # your password                                                                                                          
                         db="db")        # name of the data base                                                                                                            
                                                                                                                                                                             
    cur = db.cursor()

    cur.execute("SELECT npi, cnt FROM services limit 8500000, 382030")
    return cur.fetchall()

def getallNpis():
     db = MySQLdb.connect(host="localhost",    # your host, usually localhost                                                                                               
                         user="root",         # your username                                                                                                               
                         passwd="Galdorhavens0!",  # your password                                                                                                          
                         db="db")        # name of the data base                                                                                                             
     cur = db.cursor()

     cur.execute("SELECT npi FROM providers")

     return cur.fetchall()

def getViolationData():
    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                         user="root",         # your username
                         passwd="Galdorhavens0!",  # your password
                         db="db")        # name of the data base
    cur = db.cursor()

    cur.execute("SELECT npi FROM violations")

    return cur.fetchall()
        
    

if __name__ == "__main__":
    main()
