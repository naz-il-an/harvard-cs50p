from numb3rs import validate

def main():
    test_nums()
    test_large_num()
    test_3large()
    test_word()
    test_zero()

def test_nums():
    assert validate(r"127.0.0.1") == True
    assert validate(r"1.2.3") == False
    assert validate(r"1.2") == False
    assert validate(r"1") == False
    assert validate(r"1.2.3.1.35") == False


def test_zero():
    assert validate(r' 1255.255.256.255') == False
    assert validate(r'255.255.255.255') == True
    assert validate(r'421.1.1.1') == False



def test_large_num():
    assert validate(r"1.2.3.1000") == False

def test_3large():
    assert validate(r'127.444.0.0') == False

def test_word():
    assert validate(r"cat") == False