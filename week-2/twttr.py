def main():
    text = convert(input('Input: '))
    return text


def convert(x):
    print('Output: ', end='')
    vowels = ['a','e','o','i','u']
    for i in x:
        if i.lower() in vowels:
            continue
        else:  
            print(i, end='')

main()