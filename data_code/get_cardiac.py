import csv

def main():
    with open ('merged_personal.csv', 'rb') as f:
        with open ('cardiac_unedited.csv', 'rb') as f2:
            with open('cardiac_extracted.csv', 'wb') as m:
                next(f2)
                reader = csv.reader(f, delimiter='\t')
                readerG = csv.reader(f2)

                writer = csv.writer(m, delimiter='\t')
                pks = {}
                # add all npis from nat into set
                for row in reader:
                    name = row[1] + " " + row[2][0]
                    if row[3] != '':
                        name += ' ' 
                        name += row[3]
                    pks[name] = str(row[0]) + " " + row[6] 
                #        print row[0] + " " + name + " " + row[6]
                print len(pks) 
              
                reader2 = csv.reader(f2)
                i = 0
                for cardiac_row in reader2:
                    print cardiac_row[0]
                    if cardiac_row[0].upper() in pks:
                        i += 1 
                        print cardiac_row[0] + " found! " + pks[cardiac_row[0].upper()] 
                    elif cardiac_row[0][:-2].upper() in pks:
                        i += 1
                        print cardiac_row[0] + " found cropped! " + pks[cardiac_row[0][:-2].upper()]
                print str(i) + " found"
                #for row2 in readerG:
                 #   if row2[1] in pks:
                  #      processed = process(row2)
                   #     writer.writerow(processed)
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
