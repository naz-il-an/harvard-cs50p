def main():
    text = shorten(input('Input: '))
    print(text)


def shorten(x):
    #print('Output: ', end='')
    vowels = ['a','e','o','i','u']
    y = ''
    for i in x:
        if i.lower() not in vowels:
            y = y + i
        else:  
            continue
    return y


if __name__ == "__main__":
    main()