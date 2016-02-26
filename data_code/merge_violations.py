import csv

def main():
    with open ('merged_personal.csv', 'rb') as f:
        with open ('violations.csv', 'rb') as f2:
            with open('violations_full.csv', 'wb') as m:
                next(f)
                reader = csv.reader(f, delimiter='\t')
                writer = csv.writer(m, delimiter='\t')
                names = {}
                # add all npis from nat into set

                for row in reader:
                   # writer.writerow(row)
                    name = row[1] + ", " + row[2]
                    if row[3] != "":
                        name += " " + row[3]
#                    print name    
                    names[name] = row[0]
                reader2 = csv.reader(f2)
                for row2 in reader2:
#                    print row2[0]
                    a = row2[0].split()
                    if len(a) > 2:
                        a[-1] = a[-1][0]
                    fixed = " ".join(a)
                    if fixed.upper() in names:
#                        print fixed
                        #processed = process(row2)
                        #writer.writerow(processed)
                        #pks.add(row2[0])
                        new_row = []
                        new_row.append(names[fixed.upper()])
                        i = 5
                        while i < 9:
                            new_row.append(row2[i])
                            i += 1
                        writer.writerow(new_row)

def process(row):
    row.append('')
    row.append('')
    row.append('')
    return row

def cleanfield(field):
    return field.replace(",", "");
 



if __name__ == "__main__":
    main()
