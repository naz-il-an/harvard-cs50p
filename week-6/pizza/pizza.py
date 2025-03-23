import sys
import tabulate
import csv

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
elif sys.argv[1].endswith('.csv') == False:
    sys.exit('Not a Python file')

try:
    with open(sys.argv[1], "r") as file:
        reader = csv.reader(file, delimiter=',')
        table = tabulate.tabulate(reader, headers='firstrow')  

except FileNotFoundError:
    sys.exit('File does not exist')

print(table)