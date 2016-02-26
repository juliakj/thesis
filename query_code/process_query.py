#!/usr/bin/python
import pickle
import sys
import glob
import os

def main(argv):
    query = argv[0]

    map = getMap()

def getMap():
    for filename in os.listdir('./map_pickles'):
        print filename
   # pickle.dump(map, open('dat2.p', 'wb'))

if __name__ == "__main__":
    main(sys.argv[1:])


