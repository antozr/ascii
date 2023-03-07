
from PIL import Image
from intro import helloTxt
from inputUser import inputToUser
from functionWrite import writeFileHtml, writeFileTxt
import time


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
    
    def validatorChoiceUser():
        if choixFichier == "HTML" or choixFichier == "html" or choixFichier == "Html" or choixFichier == "TXT" or choixFichier == "txt" or choixFichier == "Txt" or choixFichier == "Both" or choixFichier == "BOTH" or choixFichier == "both":
           valueToPastCheck = True
           return valueToPastCheck
        else:
            valueToPastCheck = False
            return valueToPastCheck
            
    while validatorChoiceUser() == False:
        choixFichier = input('Enter your choice HTML / TXT / BOTH : ')
        # valueToPastCheck = True
        
    print("You have choice : "+choixFichier)
   
# chargement zone 
    print("Chargement", end="")
    for i in range(0, 10):
        time.sleep(0.5)
        print(".", end="\n")
        
# the conditions to choice write file 


    if choixFichier == "HTML" or choixFichier =="Html" or choixFichier == "html": 
        writeFileHtml(arrayAllLineHtml)
        
    elif choixFichier == "TXT" or choixFichier == "txt" or choixFichier == "Txt":
        writeFileTxt(arrayAllLine)
              
    elif choixFichier == "BOTH" or choixFichier == "Both" or choixFichier == "both":
        writeFileHtml(arrayAllLineHtml)
        writeFileTxt(arrayAllLine)
    
           
print('Thank\'s for use ASCII Convert Images ');
   
        
            
        
 
