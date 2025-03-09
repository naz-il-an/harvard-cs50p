def main():
    while True:
        try:
            x, y = input('Fraction ').split('/')
            x, y = int(x), int(y)
            fuel = round(x*100/y)
            if x > y:
                pass
            elif fuel <= 1:
                return 'E'
            elif fuel >= 99:
                return 'F'
            else:
                return f'{fuel}%'
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

print(main())