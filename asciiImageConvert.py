
from PIL import Image
from intro import helloTxt



helloTxt()

# the ascii character use for the convert 
ascii_char = '.+-$*#@'
asciiSeptante = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# the input for create a unique user image convert 
print('Enter the path of your jpeg, jpg, png with the FULL path ( whith the disk of origne ) \nExemple : C://User/desktop/myImage.png\n')
pathImage = input('Enter your url ( the full path ):')
heigthSizeImg = int(input('Choose the height of your image(just  number !!) : '))
widthSizeImg = int(input('Choose the width of your image ( just number !!) : '))
lengthDefinitionAscii = int(input("Choose de definition of your image between 10 and 69 : "))


with Image.open(pathImage ) as image:
    
    image = image.resize((heigthSizeImg,widthSizeImg))
    
    for y in range(image.height):
        line = " \n"
        for x in range(image.width) :
            rgb = image.getpixel((x, y))
            grey = sum(rgb) // len(rgb)
            index = grey * lengthDefinitionAscii // 255
            line += asciiSeptante[index] + "  "
            # to web apllication 
            # line += "<span>"+ asciiSeptante[index] + " "+"</span>"
        print(line)
        
 
