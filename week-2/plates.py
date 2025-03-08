def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    for i in s:
        if i.isalnum() == False:
            return False
    for i in range(1, len(s)):
        if s[i-1].isdigit() and s[i].isalpha():
            return False
    digits = []
    for i in s:
        if i.isdigit():
            digits.append(i)
    if digits[0] == '0':
        return False
    if  len(s) > 6 or len(s) < 2:
        return False    
    elif s[0].isdigit() or s[1].isdigit():
        return False
    elif s.isalpha():
        return True
    elif s[-1].isalpha():
        return False    
    else:
        return True    
    
main()