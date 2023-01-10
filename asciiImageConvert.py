
from PIL import Image

ascii_char = '.+-$*#@'
asciiSeptante = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
with Image.open("Frame3.png" ) as image:
    image = image.resize((500,500))
    
    for y in range(image.height):
        line = " "
        for x in range(image.width) :
            rgb = image.getpixel((x, y))
            # on fait la moyenne de chaque channel pour faire une nuance de gris
            grey = sum(rgb) // len(rgb)
            # on fait un produit en croix pour récupérer l'index
            index = grey * 69 // 255
            # on rajoute 2 espaces, car en console la hauteur d'un char est plus grande que sa largeur
            line += "<span>"+ asciiSeptante[index] + " "+"</span>"
        print(line)
        
 
