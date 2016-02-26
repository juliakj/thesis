import csv

def main():
    with open('referral.txt', 'rU') as f:
        with open ('referrals.csv', 'wb') as w:
            writer = csv.writer(w)
            count = 0
            for row in f:
                processed = extract(row)
                count = count + 1
                writer.writerow(processed);
                
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
