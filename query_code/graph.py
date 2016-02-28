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
   
    G=nx.DiGraph()
    dat = getData()
    for row in dat:
        G.add_edge(row[0], row[1], weight=row[2])

    for n in G.nodes():
        print str(n) + " " + str(G.in_degree(n))

        '''
    pos=nx.spring_layout(G) # positions for all nodes

    # nodes
    nx.draw_networkx_nodes(G,pos,node_size=200)

    # edges
    nx.draw_networkx_edges(G,pos, width=6)

    # labels
    nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')

    matplotlib.pyplot.axis('off')
    matplotlib.pyplot.savefig("weighted_graph.png") # save as png
    matplotlib.pyplot.show() # display
       '''

def getData():
    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                         user="root",         # your username
                         passwd="Galdorhavens0!",  # your password
                         db="db")        # name of the data base
    cur = db.cursor()
    cur.execute("SELECT * FROM referrals limit 100000")

    return cur.fetchall()
        
    

if __name__ == "__main__":
    main()
