import sys

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
elif sys.argv[1].endswith('.py') == False:
    sys.exit('Not a Python file')

count = 0

try:
    with open(sys.argv[1]) as file:
        lines = file.readlines()
    for line in lines:
        if line.lstrip() == '':
            count += 0
        elif line.lstrip().startswith('#'):
            count += 0
        else:
            count += 1 

except FileNotFoundError:
    sys.exit('File does not exist')

print(count)