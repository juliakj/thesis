import csv
import pickle

def main():
    with open ('npi_map.csv', 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        map = {}
        n = 0
        for row in reader:
            inNY, liscense = process(row)
            if inNY:
                print row[0]
                map[liscense] = row[0]
                n += 1
        print str(n) + " found"
        pickle.dump(map, open('ny_doctors.p', 'wb'))

 
def process(row):
    i = 49
    while i <= 105:
        if row[i] == 'NY':
            i -= 1
            return True, row[i]
        i += 4
    return False, None


if __name__ == "__main__":
    main()
