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
import networkx as nx

def main(argv):
    query = argv[0]
    state = argv[1]
    results = process_query.process(query)
    print results
    providers = getBySpecialty(results)
    filtered = filterByState(state, providers)
#    influence = getInDegree(filtered) # very slow!
    # need to rank by quality and give option to rank by cost
    print 'relevant providers found = ' + str(len(providers))
    print 'relevant providers found in state = ' + str(len(filtered))


def getInDegree(providers):
    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="Galdorhavens0!",  # your password
                     db="db")        # name of the data base

    cur = db.cursor()

    for p in providers:
        cmd = "SELECT count(*) from referrals where npi2=\'" + str(p) + "\'"
        cur.execute(cmd)
        print str(p) + " " + str(cur.fetchall()[0])


def filterByState(state, providers):
    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                        user="root",         # your username
                        passwd="Galdorhavens0!",  # your password
                        db="db")        # name of the data base
    cur = db.cursor()
    filtered = {}
    for p in providers:
        cmd = "SELECT the_state from locations where npi=\'" + str(p) + "\'"
        cur.execute(cmd)
        if cur.fetchall()[0][0] == state:
            filtered[p] = providers[p]
            filtered[p].append(state)
#            print filtered[p]
    return filtered


def getBySpecialty(spec):
    providers = {}
    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="Galdorhavens0!",  # your password
                     db="db")        # name of the data base

    cur = db.cursor()

    for s in spec:
        cmd = "SELECT npi, specialty from providers where specialty=\'" + s[0] + "\'"
        print cmd
        cur.execute(cmd)
        for row in cur.fetchall():
            providers[row[0]] = [row[1], s[1]]
    return providers


if __name__ == "__main__":
    main(sys.argv[1:])
