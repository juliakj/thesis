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

    query = argv[0]
    state = argv[1]


    results = process_query.process(query)




    # get by specialty and state
    providers = getSubset(results, state, cursor)


 #   print providers

    d = {}
    for r in results:
        d[r[0]] = r[1]
    del results

    influence = rankProviders(providers, d)

    return influence

    print influence


    print 'top 20 of all:'
    i = 0
    while i < 5:
        print influence[i]
        i += 1


    return influence


def rankProviders(providers, spec):
    for k in providers:
        providers[k].append(spec[providers[k][3]])
    sorted_res = sorted(providers.items(), key=lambda (k, v): (v[0]*.2 + v[1]*.7 + v[2]*.1)*v[-1], reverse=True)
    return sorted_res
    






def getInDegree(providers):
#    print providers
    data = pickle.load(open('/home/ubuntu/mygit/query_code/fullNetMap.p', 'rb'))

    res = {}
    for p in providers:
        if p in data:
            res[p] = providers[p] + [data[p][0], data[p][1]]
            print res[p]
#    sorted_res = sorted(res.items(), key=itemgetter(4)*itemgetter(2), reverse=True)
    sorted_res = sorted(res.items(), key=lambda (k, v): v[1]*v[3], reverse=True)
#    for s in sorted_res:
#        print s
    return sorted_res

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


def getSubset(spec, state, cur):
    providers = {}
    '''
    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="Galdorhavens0!",  # your password
                     db="db")        # name of the data base

    cur = db.cursor()
    '''
    types = "( specialty = \'" + spec[0][0] + "\'"
    for e in spec[1:]:
        types += " OR specialty = \'" + e[0] + "\'"

    types += ")"


    cmd = "SELECT npi, exp, qual, price, specialty, the_name from filters where the_state = \'" + state + "\' AND " + types
    print cmd    
    cur.execute(cmd)

    for row in cur.fetchall():
        providers[row[0]] = [row[1], row[2], row[3], row[4], row[5]]
    return providers



if __name__ == "__main__":
    get(sys.argv[1:])
