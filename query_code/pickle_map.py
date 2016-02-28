#!/usr/bin/python
import MySQLdb
import pickle
import string

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="Galdorhavens0!",  # your password
                     db="db")        # name of the data base

cur = db.cursor()

cur.execute("SELECT p.specialty, s.descrip FROM providers p, services s where p.npi=s.npi order by p.npi asc limit 1500000, 500000")

print 'selection done'

map = {}
for row in cur.fetchall():
    if row[0].upper() not in map:
        map[row[0].upper()] = row[1]
        print row[0]
    else:
        map[row[0].upper()] += " "
        map[row[0].upper()] += row[1].lower().translate(None, string.punctuation).translate(None, string.digits)
print len(map)
#for specialty in map:
#    print specialty + " " + map[specialty]
pickle.dump(map, open('dat5000004.p', 'wb'))

db.close()
