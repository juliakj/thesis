import csv

def main():
    with open ('merged_personal.csv', 'rb') as f:
        with open ('groups.csv', 'rb') as f2:
            with open('groups_extracted.csv', 'wb') as m:
                next(f2)
                reader = csv.reader(f)
                readerG = csv.reader(f2)

                writer = csv.writer(m, delimiter='\t')
                pks = set()
                # add all npis from nat into set

                for row in reader:
                    if row[10] not in pks:
                        #writer.writerow(row)
                        pks.add(row[10])
                        print row[10]
                reader2 = csv.reader(f2)
#                i  = 0
                for row2 in readerG:
                    if row2[1] in pks:
                        processed = process(row2)
                        writer.writerow(processed)
                    #    pks.add(row2[0])
 
def process(row):
    new_row = []
    new_row.append(row[1])
    new_row.append(row[0])
    new_row.append(row[5])
    new_row.append(row[7])
    new_row.append(row[9])
    new_row.append(row[11])
    return new_row

 



if __name__ == "__main__":
    main()
