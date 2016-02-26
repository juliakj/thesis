import csv

def main():
    with open('nat.csv', 'rU') as f:
        with open ('nat_personal.csv', 'wb') as w:
            reader = csv.reader(f)
            writer = csv.writer(w, delimiter='\t')
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

    if len(row) < 43:
        return new_list
    new_list.append(row[0])
    i = 3
    while i < 6:
        if i == 5:
            new_list.append(row[i][:1])
            
        else:
            new_list.append(row[i])
        i += 1
    new_list.append(row[8])
    new_list.append(row[7])
    new_list.append(row[11])
    new_list.append(row[37])
    new_list.append(row[9])
    new_list.append(row[10])
    new_list.append(row[19])
    
    return new_list;

if __name__ == "__main__":
    main()
