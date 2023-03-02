
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
arrayAllLineHtml = []
with Image.open(pathImageUser ) as image:
    
    image = image.resize((resInputUser[1],resInputUser[2]))
    
    for y in range(image.height):
        line = " "
        lineHtml = " "
        for x in range(image.width) :
            rgb = image.getpixel((x, y))
            grey = sum(rgb) // len(rgb)
            index = grey * resInputUser[3] // 255
            line += asciiSeptante[index] + "  "
            # to web apllication 
            lineHtml += "<span>"+ asciiSeptante[index] + " "+"</span>"
        
       # print(line)
        arrayAllLine.append(line)
        arrayAllLineHtml.append(lineHtml)
    #print(arrayAllLine)
    #print all line in text file
    
    print('Tu veux un rendu en fichier HTML / TXT ou les deux ? \n')
    choixFichier = input('Enter your choice HTML / TXT / BOTH : ')
    with open('imageArt.txt', 'w') as file :
        for arrayLine in arrayAllLine:
            file.write(arrayLine)
            file.write('\n')
            
    with open('ascii.html', 'w') as file :
        file.write('<span style="color:black; font-size:8px; font-family:\'Consolas\',\'BitstreamVeraSansMono\',\'CourierNew\',Courier,monospace; display:inline-block; white-space:pre; "> \n')
        
        for arrayLine in arrayAllLineHtml:
            file.write(arrayLine) 
            file.write('\n') 
            
        file.write('</span>')
        
            
        
 
