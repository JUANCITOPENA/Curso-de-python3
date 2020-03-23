import csv

doc_csv = open("csv_file.csv", "w")

csv_data = csv.writer(doc_csv)
lista = ["jose", 1000000001]

csv_data.writerow(lista)
doc_csv.close()