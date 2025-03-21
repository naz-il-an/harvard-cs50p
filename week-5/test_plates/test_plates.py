from plates import is_valid

def main():
    test_valid()
    test_invalid()
    test_end_letter()
    test_numbers()
    test_length()
    test_alpha_num()

def test_valid():
    assert is_valid('CS50') == True
    assert is_valid('Ilyas') == True

def test_invalid():
    assert is_valid('cs05') == False

def test_end_letter():
    assert is_valid('Aa12') == True
    assert is_valid('A123') == False
    assert is_valid('NY11C') == False

def test_numbers():
    assert is_valid('1111') == False

def test_length():
    assert is_valid('Myplate') == False

def test_alpha_num():
    assert is_valid('Af1.') == False


if __name__ == '__main__':
    main()
