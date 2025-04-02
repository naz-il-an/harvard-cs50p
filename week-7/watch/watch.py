import re

def main():
    print(parse(input('HTML: ').strip()))

def parse(url):
    matches = re.search(r'src="https://(?:www\.)youtu\.?be(?:\.com)?/embed/(\w+)"', url, re.IGNORECASE)
    if matches:
        name = 'https://youtu.be/' + matches.group(1)
        return name

if __name__ == '__main__':
    main()