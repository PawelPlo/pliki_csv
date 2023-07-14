import sys
import csv
import json
import pickle

class Reader:
    def changer (self):
        argumenty_zmian = sys.argv[3:]
        numer_argumentu = 1
        slownik_zmian = {}
        for row in argumenty_zmian:
            row = row.strip(",")
            slownik_zmian[numer_argumentu] = row
            row = row.split(",")
            for linia in content:
                for k in row:
                    content[int(row[0])][int(row[1])] = row[2]
                    numer_argumentu += 1

class CSVHandler(Reader):
    def pobieranie_danych_z_pliku(self, file_path):
        self.file_path = file_path
        with open(file_path) as plik:
            reader = csv.reader(plik)
            for line in reader:
                content.append(line)

    def zapisywanie_do_pliku(self, target_file_path):
        self.target_file_path = target_file_path
        with open(target_file_path, "w", newline="") as plik:
            writer = csv.writer(plik)
            for line in content:
                writer.writerow(line)


class JsonHandler(Reader):
    def pobieranie_danych_z_pliku(self, file_path):
        self.file_path = file_path
        with open (file_path, "r") as f:
            return json.load(f)



    def zapisywanie_do_pliku(self, target_file_path, obj):
        self.target_file_path = target_file_path
        self.obj = obj
        with open(target_file_path, "w") as f:
            json.dump(obj, f)
class PickleHandler(Reader):
    def pobieranie_danych_z_pliku(self, file_path):
        self.file_path = file_path
        with open (file_path, "rb") as f:
            return pickle.load(f)

    def zapisywanie_do_pliku(self, target_file_path, obj):
        self.target_file_path = target_file_path
        self.obj = obj
        with open(target_file_path, "wb") as f:
            pickle.dump(obj, f)
class TxtHandler(Reader):
    def pobieranie_danych_z_pliku(self, file_path):
        self.file_path = file_path
        with open(file_path, "r") as plik:
            for line in plik:
                content.append(line)

    def zapisywanie_do_pliku(self, target_file_path):
        self.target_file_path = target_file_path
        with open(target_file_path, "w") as plik:
            for line in content:
                plik.write(f"{line}\n")

content = []

if sys.argv[1].endswith(".csv"):
    zmiana = CSVHandler()
    zmiana.pobieranie_danych_z_pliku(file_path = sys.argv[1])
    zmiana.changer()
elif sys.argv[1].endswith(".json"):
    zmiana = JsonHandler()
    zmiana.pobieranie_danych_z_pliku(file_path=sys.argv[1])
    content = zmiana.pobieranie_danych_z_pliku(file_path=sys.argv[1])
    zmiana.changer()
elif sys.argv[1].endswith(".pickle"):
    zmiana = PickleHandler()
    zmiana.pobieranie_danych_z_pliku(file_path=sys.argv[1])
    zmiana.changer()
elif sys.argv[1].endswith(".txt"):
    zmiana = TxtHandler()
    zmiana.pobieranie_danych_z_pliku(file_path=sys.argv[1])
    zmiana.changer()


print('Dane z pliku "in.json"')
for row in content:
    print(row)
print('\n\nDane do pliku "out.csv"')
for row in content:
    print(row)


print('''Wybierz format zapisu zmian:
CSV - wybierz: "1"
Json - wybierz: "2"
Pickle - wybierz: "3"
Txt - wybierz: "4"
''')
wybor = input()

while True:
    if wybor != "1" and wybor != "2" and wybor != "3" and wybor !="4":
        print("Nie wpisałeś poprawnie numeru wyboru! Spróbuj raz jeszcze")
        continue
    if wybor == "1":
        zmiana = CSVHandler()
        zmiana.zapisywanie_do_pliku(target_file_path = sys.argv[2])
        break
    if wybor == "2":
        zmiana = JsonHandler()
        zmiana.zapisywanie_do_pliku(target_file_path = "out.json", obj=content)
        break
    if wybor == "3":
        zmiana = PickleHandler()
        zmiana.zapisywanie_do_pliku(target_file_path="out.pickle", obj=content)
        break
    if wybor == "4":
        zmiana = TxtHandler()
        zmiana.zapisywanie_do_pliku(target_file_path="out.txt")
        break


