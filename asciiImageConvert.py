
from PIL import Image

ascii_char = '.+-$*#@'
asciiSeptante = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
pathImage = input('Enter your url ( the full path ):')
heigthSizeImg = int(input('Choose the height of your image(just  number) : '))
widthSizeImg = int(input('Choose the width of your image ( just number !!) : '))
with Image.open(pathImage ) as image:
    
    image = image.resize((heigthSizeImg,widthSizeImg))
    
    for y in range(image.height):
        line = " "
        for x in range(image.width) :
            rgb = image.getpixel((x, y))
            grey = sum(rgb) // len(rgb)
            index = grey * 69 // 255
            line += asciiSeptante[index] + "  "
            # to web apllication 
            # line += "<span>"+ asciiSeptante[index] + " "+"</span>"
        print(line)
        
 
