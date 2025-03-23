import sys
import csv

def main():
    old_file = csv_read()
    new_file = write_new(old_file)
    return new_file
    

if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')
elif sys.argv[1].endswith('.csv') == False:
    sys.exit('Not a Python file')

def csv_read():
    after = []
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                last, first = row['name'].split(sep=',')
                after.append({'first': first.strip(),'last': last, 'house': row['house']})
            return after            
        
    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')

def write_new(x):
    with open(sys.argv[2], 'w') as new_file:
        writer = csv.DictWriter(new_file, fieldnames=['first', 'last', 'house'])
        writer.writeheader()
        for row in x:
            writer.writerow({'first': row['first'], 'last': row['last'], 'house': row['house']})

main()