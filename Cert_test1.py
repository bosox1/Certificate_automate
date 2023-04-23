import csv
import PyPDF2

with open("Cerf_csv.csv", encoding='utf-8') as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} {row[1]} {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')