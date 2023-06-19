import sys
import csv


file_path = sys.argv[1]
target_file_path = sys.argv[2]

content = []

with open(file_path) as plik:
   reader = csv.reader(plik)
   for line in reader:
       content.append(line)

print('Dane z pliku "in.csv"')
for row in content:
    print(row)

argumenty_zmian = sys.argv[3:]
numer_argumentu = 1
slownik_zmian = {}
for row in argumenty_zmian:
    row = row.strip(",")
    slownik_zmian[numer_argumentu]=row
    row = row.split(",")
    for linia in content:
        for zmiana in row:
                content[int(row[0])][int(row[1])] = row[2]
                numer_argumentu += 1

print('\n\nDane do pliku "out.csv"')
for row in content:
    print(row)

with open(target_file_path, "w", newline = "") as plik:
    writer = csv.writer(plik)
    for line in content:
        writer.writerow(line)
