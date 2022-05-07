import csv


class MyDialect(csv.Dialect):
    quoting = csv.QUOTE_ALL
    quotechar = " "  # заполнение пустоты
    delimiter = "."  # знаки перечисления
    lineterminator = '\n'


csv.register_dialect('EasyDialect', MyDialect)

with open('output.csv', 'w') as f:
    write = csv.writer(f, dialect='EasyDialect')
    write.writerow(['4', '80', '97'])
    write.writerow(['65', '91', '71'])
    write.writerow(['86', '60', '57'])
    write.writerow(['67', '33', '99'])
    write.writerow(['89', '5', '53'])

with open('output.csv', 'r') as f:
    read = csv.reader(f)
    for row in read:
        print(row)

