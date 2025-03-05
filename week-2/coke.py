cost = 50
print('Amount Due:', cost)

while cost > 0:
    insert = int(input('Insert Coin: '))
    if insert in [5, 10, 25]:
        cost -= insert
        if cost <= 0:
            break
    print('Amount Due:', cost)

print('Change Owed:', abs(cost))