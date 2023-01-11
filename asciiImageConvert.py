
from PIL import Image
from intro import helloTxt
from inputUser import inputToUser


helloTxt()

# the ascii character use for the convert 
ascii_char = '.+-$*#@'
asciiSeptante = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# the input for create a unique user image convert 
resInputUser= inputToUser()
pathImageUser= resInputUser[0]
arrayAllLine = []

with Image.open(pathImageUser ) as image:
    
    image = image.resize((resInputUser[1],resInputUser[2]))
    
    for y in range(image.height):
        line = " "
        for x in range(image.width) :
            rgb = image.getpixel((x, y))
            grey = sum(rgb) // len(rgb)
            index = grey * resInputUser[3] // 255
            line += asciiSeptante[index] + "  "
            # to web apllication 
            # line += "<span>"+ asciiSeptante[index] + " "+"</span>"
        
        print(line)
        arrayAllLine.append(line)
    print(arrayAllLine)
    #print all line in text file
    with open('imageArt.txt', 'w') as file :
        for arrayLine in arrayAllLine:
            file.write(arrayLine)
            file.write('\n')
        
        
            
        
 
