def new_main():
    camel = input('camelCase: ')

    print('snake_case: ', end='')
    for i in camel:
        if i.isupper():
            i = '_' + i.lower()
        print(i, end = '')

new_main()