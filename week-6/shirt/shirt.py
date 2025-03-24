import sys
from PIL import Image, ImageOps
from os.path import splitext

def main():
    check_input()
    combine()
    
def check_input():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    # elif (sys.argv[1].endswith('.png') and sys.argv[2].endswith('.png')) or (sys.argv[1].endswith('.jpg') and sys.argv[2].endswith('.jpg')):
    #     return True
    # elif (sys.argv[1].endswith('.png') and sys.argv[2].endswith('.jpg')) or (sys.argv[1].endswith('.jpg') and sys.argv[2].endswith('.png')):
    #     sys.exit('Input and output have different extensions')
    # elif sys.argv[1].endswith('.png') == False or sys.argv[2].endswith('.png') == False or sys.argv[1].endswith('.jpg') == False or sys.argv[2].endswith('.jpg') == False:
    #     sys.exit('Invalid input')

    a1, b1 = splitext(sys.argv[1])
    a2, b2 = splitext(sys.argv[2])
    extensions = ['.jpg', '.jpeg', '.png']
    if b1 == b2:
        return True
    elif b1 not in extensions or b2 not in extensions:
        sys.exit('Invalid input')
    elif b1 != b2:
        sys.exit('Input and output have different extensions')

def combine():
    try:
        face = Image.open (sys.argv[1]) 
        shirt = Image.open('shirt.png')            
        size = shirt.size
        face = ImageOps.fit(face, size)
        face.paste(shirt, box = (0,0), mask = shirt)
        face.save(sys.argv[2])
        return face
    
    except FileNotFoundError:
        sys.exit('Input does not exist')

main()