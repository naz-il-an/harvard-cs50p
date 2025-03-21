def main():
    fuel_fraction = convert(input('Fraction: '))
    print(gauge(fuel_fraction))


def convert(fraction):
    while True:
        try:            
            x, y = fraction.split('/')
            x, y = int(x), int(y)
            fuel_perc = round(x*100/y)
            if x > y:
                fraction = input('Fraction: ')
                pass
            return fuel_perc
        except ValueError:
            raise
        except ZeroDivisionError:
            
            raise        

def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f'{percentage}%'


if __name__ == "__main__":
    main()
