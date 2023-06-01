import numpy as np
from PIL import Image
def get_type(file):
    return file.split(".")[1]

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
arr = np.array(convert_text_to_rgb("C:\\Users\\Bisrat worku\\Desktop\\ssd.txt"))
img = Image.fromarray(arr.astype('uint8')).convert('RGB')
img.save('super.png')

