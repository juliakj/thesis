import csv

def main():
    with open ('personal_util.csv', 'rb') as f:
        # changed from unedited_util
        with open('util_no_dups.csv', 'wb') as w:
            next(f)
            reader = csv.reader(f, delimiter='\t')
            writer = csv.writer(w, delimiter='\t')
            pks = set()
            for row in reader:
                if row[0] not in pks:
                    writer.writerow(row)
                    pks.add(row[0])

 



if __name__ == "__main__":
    main()
