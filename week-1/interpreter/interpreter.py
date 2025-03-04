expression = input('Expression ').split()
x = int(expression[0])
y = int(expression[2])

if '+' in expression:
    print(float(x + y))
elif '-' in expression:
    print(float(x - y))
elif '*' in expression:
    print(float(x * y))
else:
    print(float(x / y))