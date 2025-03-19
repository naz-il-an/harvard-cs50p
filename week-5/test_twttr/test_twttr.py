from twttr import shorten

def main():
    test_shorten()
    test_num()
    test_punct()

def test_shorten():
    assert shorten('twitter') == 'twttr'
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('TwItTeR') == 'TwtTR'

def test_num():
    assert shorten('1234') == '1234'

def test_punct():
    assert shorten('!?.,') == '!?.,'

if __name__ == "__main__":
    main()
