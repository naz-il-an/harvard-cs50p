import random


def main():
    score = 0
    round = 0
    n = get_level()
    
    while round != 10:
        round += 1
        wrong_ans = 0
        
        x, y = generate_integer(n), generate_integer(n)                
        answer = x + y
        
        while True:
            try:
                user_ans = int(input(f'{x} + {y} = '))
                if answer == user_ans:
                    score += 1
                    break
                else:
                    print('EEE')
                    wrong_ans += 1
                    pass
                if wrong_ans == 3:
                    print(f'{x} + {y} = {answer}')
                    break
            except ValueError:
                pass      
        pass
    print (score)


def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level == 1 or level==2 or level==3:
                return level
            else:
                pass   
        except ValueError:
            pass         


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    

if __name__ == "__main__":
    main()