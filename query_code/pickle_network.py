#!/usr/bin/python
import MySQLdb
import pickle
import string
import sys
import operator

def main(args):
	start = args[0]
	num = args[1]

	db = MySQLdb.connect(host="localhost",    # your host, usually localhost
	                     user="root",         # your username
	                     passwd="Galdorhavens0!",  # your password
	                     db="db")        # name of the data base

	cur = db.cursor()

	cmd = "SELECT * FROM referrals limit " + str(start) + ", " + str(num) #1500000, 500000"
	cur.execute(cmd)

	print 'selection done'

	map = {}
	for row in cur.fetchall():
	    if row[0] not in map:
	    	map[row[0]] = (0, 0)
	    if row[1] not in map:
	    	map[row[1]] = (0, 0)

	    map[row[0]] = tuple(map(operator.add, map[row[0]], (1,row[2])))
	    map[row[1]] = tuple(map(operator.add, map[row[1]], (1,row[2])))
	      	
	print len(map)

	for p in map:
		print str(p) + " : "
		print map[p]

	name = "dat" + str(start) + "-" + str(start+num) + ".p"
	pickle.dump(map, open(name, 'wb'))

	db.close()

if __name__ == "__main__":
 	main(sys.argv[1:])
