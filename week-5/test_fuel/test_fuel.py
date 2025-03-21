from fuel import convert, gauge

def main():
    test_convert()
    test_gauge()

def test_convert():
    assert convert('3/4') == 75

def test_gauge():
    assert gauge(75) == '75%'
    assert gauge(100) == 'F'

if __name__ == '__main__':
    main()
