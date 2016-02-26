import csv
# extract personal data from util set
def main():
    with open('unedited_util.txt', 'rU') as f:
        with open ('personal_util.csv', 'wb') as w:
            next(f)
            reader = csv.reader(f, delimiter='\t')
            writer = csv.writer(w, delimiter='\t')
            count = 0
            skipped = 0
            for row in reader:
                processed, skipped = extract(row, skipped)
                count = count + 1
                if processed:
                    writer.writerow(processed);
                
            print count
            print skipped

def extract(row, skipped):
    # remove un-needed fields
    new_list = []

    if (row[5] != ''):
        #new_list.append(row[0:6])
        i = 0
        while i < 6:
            new_list.append(row[i])
            i += 1
        new_list.append(row[13])
        new_list.append(row[14])
    else:
        skipped = skipped + 1
    return new_list, skipped;

if __name__ == "__main__":
    main()
