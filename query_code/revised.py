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



def get(argv, cursor):

    # testing to see if sql breaks!

    query = argv[0]
    state = argv[1]
    results = process_query.process(query)
    print results
    providers = getBySpecialty(results, cursor)
    filtered = filterByState(state, providers, cursor)
    influence = getInDegree(filtered)
    # need to rank by quality and give option to rank by cost
    '''
    print 'relevant providers found = ' + str(len(providers))
    print 'relevant providers found in state = ' + str(len(filtered))


    print 'top 20 of all:'

    i = 0
    while i < 5:
        print influence[i]
        i += 1

    '''
    return influence

def getInDegree(providers):
#    print providers
    data = pickle.load(open('/home/ubuntu/mygit/query_code/fullNetMap.p', 'rb'))

    res = {}
    for p in providers:
        if p in data:
            res[p] = providers[p] + [data[p][0], data[p][1]]
            print res[p]
#    sorted_res = sorted(res.items(), key=itemgetter(4)*itemgetter(2), reverse=True)
    sorted_res = sorted(res.items(), key=lambda (k, v): v[1]*v[4], reverse=True)
#    for s in sorted_res:
#        print s
    return sorted_res

def filterByState(state, providers, cur):
    filtered = {}
    for p in providers:
        cmd = "SELECT the_state from locations where npi=\'" + str(p) + "\'"
        cur.execute(cmd)
        if cur.fetchall()[0][0] == state:
            filtered[p] = providers[p]
            filtered[p].append(str(state))
#            print filtered[p]
    return filtered


def getBySpecialty(spec, cur):
    providers = {}

    for s in spec:
        cmd = "SELECT npi, specialty, firstname, lastname from providers where specialty=\'" + s[0] + "\'"
        print cmd
        cur.execute(cmd)
        for row in cur.fetchall():
            name = row[2] + " " + row[3]
            providers[row[0]] = [str(row[1]), s[1], str(name)] # also get the name
    return providers


if __name__ == "__main__":
    get(sys.argv[1:])
