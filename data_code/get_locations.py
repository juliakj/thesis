import csv

def main():
    with open('nat.csv', 'rU') as f:
        with open ('nat_locations.csv', 'wb') as w:
            next(f)
            reader = csv.reader(f)
            writer = csv.writer(w, '\t')
            count = 0
            for row in reader:
                processed = extract(row)
                if processed:
                    count = count + 1
                    writer.writerow(processed);
                
            print count
        

def extract(row):
    # remove un-needed fields
    new_list = []

    if len(row) < 26:
        return new_list
    new_list.append(row[0]);
    if row[22] != '':
        new_list.append(row[21] + " " + row[22])
        print new_list[1]
    else:
        new_list.append(row[21])
    new_list.append(row[24])
    new_list.append(row[26])
    new_list.append(row[25])


    return new_list;

if __name__ == "__main__":
    main()
