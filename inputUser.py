

def inputToUser(): 
    print('Enter the path of your jpeg, jpg, png with the FULL path ( whith the disk of origne ) \nExemple : C://User/desktop/myImage.png\n')
    pathImage = input('Enter your url ( the full path ):')
    heigthSizeImg = int(input('Choose the height of your image(just  number !!) : '))
    widthSizeImg = int(input('Choose the width of your image ( just number !!) : '))
    lengthDefinitionAscii = int(input("Choose de definition of your image between 10 and 69 : "))
    return [pathImage, heigthSizeImg, widthSizeImg, lengthDefinitionAscii]
