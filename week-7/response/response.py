import validator_collection as vc

def main():
    print(check(input("What's your email address? ")))

def check(url):
    try:
        vc.email(url, allow_empty=True)
        return 'Valid'
    except vc.errors.InvalidEmailError:
        return 'Invalid'

if __name__ == '__main__':
    main()