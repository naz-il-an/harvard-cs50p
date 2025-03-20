from bank import value

def main():
    test_hello()

def test_hello():
    assert value('Hello') == '$0'

def test_hi():
    assert value('Hi') == '$20'

def test_others():
    assert value('Ciao') == '$100'

if __name__ == '__main__':
    main()