from fuel import convert, gauge
import pytest

def main():
    test_convert()
    test_gauge()
    test_valueerror()
    test_zero()

def test_convert():
    assert convert('3/4') == 75

def test_valueerror():
    with pytest.raises(ValueError):
        convert('c/v')

def test_zero():
     with pytest.raises(ZeroDivisionError):
         convert('1/0')
def test_gauge():
    assert gauge(75) == '75%'
    assert gauge(99) == 'F'
    assert gauge(1) == 'E'

if __name__ == '__main__':
    main()