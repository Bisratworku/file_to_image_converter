import numpy as np
from PIL import Image

print("Input the path of the file you want to convert")
path = input(">")
def path_formatter(path):
    arr = path.split('\\')
    first_element = arr[0]
    Remove_first = arr.pop(0) # this code will remove the first element form array b/c we need to split it again
    first_element = first_element.split(':')
    arr = []
    for i in arr:
        arr.append(f'\\\{i}')    
    separate_elements = ''
    output = f'{first_element[0]}:\\\{first_element[1]}{separate_elements.join(sad)}'
    return output
path_formatter(path)
def convert_text_to_rgb(file):
    binary = []
    with open(file)as content:
        s = content.read()
    for i in s:
        convert = ord(i)
        binary.append(convert)
    remander = 0
    if not len(binary)%3 == 0:
        remander = len(binary)
    for i in range(remander + 2):
        binary.append(i)
    binary = np.array(binary)
    reshape = binary.reshape(-1,3)
    return reshape 
arr = np.array(convert_text_to_rgb(path_formatter))
img = Image.fromarray(arr.astype('uint8')).convert('RGB')
img.save('img.png')
