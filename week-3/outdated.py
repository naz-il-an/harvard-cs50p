def main():
    
    month = monthes()
    while True:
        user_date = input('Date: ')
        if '/' in user_date:
            m, d, y = user_date.split(sep='/')
            if m.isalpha():
                pass
            else:
                m, d, y = int(m), int(d), int(y)
                if d > 31 or m > 12:
                    pass
                else:
                    print(f'{y}-{m:02}-{d:02}')
                    break
        elif ',' in user_date:
            m, d, y = user_date.split()
            if m.isalpha():
                m, d, y = m.title(), int(d[:-1]), int(y)
                if d > 31 or m not in month:
                    pass
                elif m in month:
                    m = month.index(m)
                    print(f'{y}-{m+1:02}-{d:02}')
                    break
            else:
                pass
        else:
            pass

def monthes():

    monthes = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ] 
    return monthes

main()