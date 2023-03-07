
import webbrowser

def writeFileHtml(arrayAllLineHtml) :
    with open('ascii.html', 'w') as file :
            file.write('<span style="color:black; font-size:8px; font-family:\'Consolas\',\'BitstreamVeraSansMono\',\'CourierNew\',Courier,monospace; display:inline-block; white-space:pre; "> \n')
            
            for arrayLine in arrayAllLineHtml:
                file.write(arrayLine) 
                file.write('\n') 
                
            file.write('</span>')
    webbrowser.open("ascii.html")
def writeFileTxt (arrayAllLine):
    with open('imageArt.txt', 'r+') as file:
            file.truncate(0)
    with open('imageArt.txt', 'w') as file :
        for arrayLine in arrayAllLine:
            file.write(arrayLine)
            file.write('\n')