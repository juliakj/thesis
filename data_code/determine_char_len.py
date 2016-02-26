import csv

def main():
    with open ('service_util.csv', 'rb') as f:
        #next(f)
        reader = csv.reader(f)
        lengths = [0, 0]
        for row in reader:
            counts, data = extract(row)
            i = 0;
            while i < 1:
                if counts[i] > lengths[i]:
                    lengths[i] = counts[i];
                    print i, data[i];
                i = i + 1;
        print lengths
 

def extract(row):
    counts = []
    data = []
    counts.append(len(row[2]));
 #   counts.append(len(row[3]));
#    counts.append(len(row[2]));
#    counts.append(len(row[4]));
#    counts.append(len(row[6]));
    data.append(row[2])
#    data.append(row[3])
#    data.append(row[2])
#    data.append(row[4])
#    data.append(row[6])
    return counts, data;


if __name__ == "__main__":
    main()
