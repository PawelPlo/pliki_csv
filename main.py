import sys
import csv

print(sys.argv)

file_path = "in.csv"
target_file_path = "out.csv"

content = []

with open(file_path) as plik:
   reader = csv.reader(plik)
   for line in reader:
       content.append(line)

print('Dane z pliku "in.csv"')
for row in content:
    print(row)


content[int(sys.argv[3])][int(sys.argv[4])] = sys.argv[5]
content[int(sys.argv[7])][int(sys.argv[6])] = sys.argv[8]
content[int(sys.argv[10])][int(sys.argv[9])] = sys.argv[11]
content[int(sys.argv[13])][int(sys.argv[12])] = sys.argv[14]


print('\n\nDane do pliku "out.csv"')
for row in content:
    print(row)

with open(target_file_path, "w", newline = "") as plik:
    writer = csv.writer(plik)
    for line in content:
        writer.writerow(line)
