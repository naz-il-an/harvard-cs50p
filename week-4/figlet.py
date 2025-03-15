from pyfiglet import Figlet
import sys
import random
figlet = Figlet()

rand_font = random.choice(figlet.getFonts())
figlet.setFont(fond = rand_font)

if len(sys.argv) < 3 or sys.argv[1]!='-f':
    sys.exit('Invalid usage')

elif len(sys.argv) == 3:
    figlet.setFont(font=sys.argv[2])
s =input('Input: ') 

s =input('Input: ')  

if s == '':
    sys.exit('Invalid usage')

print(figlet.renderText(s))