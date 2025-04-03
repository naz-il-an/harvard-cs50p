from um import count

def main():
    test_count()

def test_count():
    assert count('um') == 1
    assert count('um?') == 1
    assert count('Um, thanks') == 1
    assert count('Um, oh um hello') == 2

def test_zero_count():
    assert count('yummy') == 0
    assert count('yum') == 0

if __name__ == '__main__':
    main()