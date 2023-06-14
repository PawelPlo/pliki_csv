import csv

file_path = "in.csv"
target_file_path = "out.csv"

content = []

with open(file_path) as plik:
   reader = csv.reader(plik)
   for line in reader:
       content.append(line)

print(content)

lista_1 = content[0]
lista_1[0] = "gitara"
lista_2 = content[1]
lista_2[3] = "kubek"
lista_3 = content[2]
lista_3[1] = "17"
lista_4 = content[3]
lista_4[3] = "0"

with open(target_file_path, "w", newline = "") as plik:
    writer = csv.writer(plik)
    for line in content:
        writer.writerow(line)
