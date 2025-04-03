import re
import sys

def main():
    print(count(input("Text: ")))


def count(s):
    s = s.lower()
    ums = re.findall(r'\bum\b', s)
    count = len(ums)

    return count


if __name__ == "__main__":
    main()