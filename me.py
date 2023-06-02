import csv
with open('data.csv','r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    semua = list(csv_reader)
    print(semua)