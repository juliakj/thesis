#!/usr/bin/python
import pickle
import sys
import glob
import os

def main(argv):
    query = argv[0]

    map = getMap()

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

if __name__ == "__main__":
    main(sys.argv[1:])


