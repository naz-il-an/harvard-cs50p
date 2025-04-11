from seasons import convert_date


def main():
    test_one_year()
    test_two_year()


def test_one_year():
    assert convert_date('2024-04-11') == 'Five hundred twenty-five thousand, six hundred minutes'

def test_two_year():
    assert convert_date('2023-04-11') == 'One million, fifty-two thousand, six hundred forty minutes'


if __name__ == '__main__':
    main()