import random

def main():
    n = rand_level()    
    while True:
        try:
            guess_num = int(input('Guess: '))
            if n == guess_num:
                print('Just right!')
                break
            elif n <= guess_num:
                print('Too large!')
                pass
            elif n >= guess_num:
                print('Too small!')
                pass
            else:
                pass 
        except ValueError:
            pass       

def rand_level():
    while True:
        try:
            level_num = int(input('Level: '))
            if level_num < 0:
                    pass
            n = random.randint(1, level_num)
            return n
        except ValueError:
            pass

main()