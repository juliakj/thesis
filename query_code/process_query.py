#!/usr/bin/python
import pickle
import sys
import glob
import os
import nltk

def main(argv):
    query = argv[0]

    map = getMap()
    top = getTopFrequencies(map)

def getMap():
	path = './map_pickles'
	full = {}
	for filename in os.listdir(path):
		temp = pickle.load(open(path + '/' + filename, 'rb'))
		for specialty in temp:
			if specialty not in full:
				full[specialty] = temp[specialty]
			else:
				full[specialty] += " "
				full[specialty] += temp[specialty]
	print len(full)

def getTopFrequencies(map):
	for specialty in map:
		allWords = nltk.tokenize.word_tokenize(map[specialty])

if __name__ == "__main__":
    main(sys.argv[1:])


