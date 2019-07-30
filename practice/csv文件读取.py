import csv
with open("C:\\Users\\linzi\\Desktop\\test.csv",'r') as f:

    file=csv.reader(f)
# print(file)
    for stu in file:
        print(stu)
