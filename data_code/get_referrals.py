import csv

def main():

    with open('referral.txt', 'rU') as f:
        with open ('referrals.csv', 'wb') as w:
            with open ('merged_personal.csv', 'rU') as providers:
                reader = csv.reader(providers, delimiter='\t')
                npi = set()
                for row in reader:
                    npi.add(row[0])
                writer = csv.writer(w)
                count = 0
                rm = 0
                for row in f:
                    processed = extract(row)
                    
                    if processed[0] in npi and  processed[1] in npi:
                        writer.writerow(processed);
                        count += 1
                print count

        

def extract(row):
    split = [x.strip() for x in row.split(',')]

    new_list = []
    new_list.append(split[0])
    new_list.append(split[1])
    new_list.append(split[2])

    return new_list;

if __name__ == "__main__":
    main()
