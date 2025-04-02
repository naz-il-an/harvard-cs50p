import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(r'(\d{1,2}):?([0-5]?[0-9])? am (?:to|:) (\d{1,2}):?([0-5]?[0-9])? pm', s, re.IGNORECASE)
    if match and int(match.group(1))<13 and int(match.group(3))<13:
        starthour, endhour = int(match.group(1)), int(match.group(3)) + 12
        if match.group(2):
            startmin = int(match.group(2))
        else:
            startmin = 0
        if match.group(4):
            endmin = match.group(4)
        else:
            endmin = 0
        if starthour == 12:
            starthour = 0
        if endhour == 24:
            endhour = 12
        time = f'{starthour:02}:{startmin:02} to {endhour:02}:{endmin:02}'

        return time


    match = re.search(r'(\d{1,2}):?([0-5]?[0-9])? pm (?:to|:) (\d{1,2}):?([0-5]?[0-9])? am', s, re.IGNORECASE)
    if match and int(match.group(1))<13 and int(match.group(3))<13:
        starthour, endhour = int(match.group(1)) + 12, int(match.group(3))
        if match.group(2):
            startmin = int(match.group(2))
        else:
            startmin = 0
        if match.group(4):
            endmin = int(match.group(4))
        else:
            endmin = 0
        time = f'{starthour:02}:{startmin:02} to {endhour:02}:{endmin:02}'

        return time
    else:
        raise ValueError


if __name__ == "__main__":
    main()