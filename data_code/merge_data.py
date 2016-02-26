import csv

def main():
    with open ('nat_personal.csv', 'rb') as f:
        with open ('util_no_dups.csv', 'rb') as f2:
            with open('merged_personal.csv', 'wb') as m:
                next(f)
                reader = csv.reader(f, delimiter='\t')
                writer = csv.writer(m, delimiter='\t')
                pks = set()
                # add all npis from nat into set

                for row in reader:
                    if row[0] not in pks:
                        writer.writerow(row)
                        pks.add(row[0])
                    else:
                        print "repeat " + row[0]
                reader2 = csv.reader(f2, delimiter='\t')
                for row2 in reader2:
                    if row2[0] not in pks:
                        print row2[0]
                        processed = process(row2)
                        writer.writerow(processed)
                        pks.add(row2[0])

def process(row):
    row.append('')
    row.append('')
    row.append('')
    return row

 



if __name__ == "__main__":
    main()
