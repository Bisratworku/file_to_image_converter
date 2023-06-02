from PIL import Image
import numpy as np
im = Image.open('superm.png')
mat = np.array(im)
s = []
for i in range(len(mat)):
    for j in range(len(mat[i])):
        s.append(mat[i][j])
f = []
g = []
for i in s:
    f.append(i[0])
#'\x00':
for i in f:
    g.append(chr(i))
print(g)



