from PIL import Image
import numpy as np
file_with_extention = input('input the file you want to convert')
name = file_with_extention.split('.')[0]
print(name)
def convert_to_txt(file):
    im = Image.open(file)
    metrix = np.array(im)
    spread = []
    for i in range(len(metrix)): #metrix is a 2d array and one element contains three 1d arrays each element of array is the same so this loop will append those arrays flatten() is it will make the array 1d and it will be hard to remove duplicates. 
        for j in range(len(metrix[i])):
            spread.append(metrix[i][j])
    Take_the_firatrow = []
    stringfy = []
    text = ''
    for i in spread:#from that array we only need the first element
        Take_the_firatrow.append(i[0])
    for i in Take_the_firatrow:
        stringfy.append(str(chr(i)))#in here we convert aclii code to a character
    for i in stringfy: #in here we filter all the null aclii code this will get us only the chatracters we want
        if i == '\x00':
            break
        else:
            text = text + i
    return text
#files = open(f'{name}','x')
#files.write(convert_to_txt(f'{file_with_extention}.png'))