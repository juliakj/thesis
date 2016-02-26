import csv

def main():
    with open ('nat_locations.csv', 'rb') as f:
        with open ('loc_util_no_dups.csv', 'rb') as f2:
            with open('merged_locations.csv', 'wb') as m:
                reader = csv.reader(f)
                writer = csv.writer(m)
                pks = set()
                # add all npis from nat into set
                for row in reader:
                    if row[0] not in pks:
                        writer.writerow(row)
                        pks.add(row[0])
                reader2 = csv.reader(f2)
                for row2 in reader2:
                    if row2[0] not in pks:
                        print row2[0]
                        processed = process(row2)
                        writer.writerow(processed)

def process(row):
    return row

 



if __name__ == "__main__":
    main()
