
from PIL import Image

ascii_char = '.+-$*#@'
asciiSeptante = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
with Image.open("Frame 3.png" ) as image:
    image = image.resize((500,500))
    
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
        
 
