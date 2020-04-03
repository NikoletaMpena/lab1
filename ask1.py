import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

if len(sys.argv) > 1:
    img = cv2.imread(sys.argv[1])
    newImg = sys.argv[2]
    threshold = int(sys.argv[3])
    
else:
    exit(1)
    
    
outImg = np.copy(img)
colored = 0

height = outImg.shape[0]
width = outImg.shape[1]

white = [255,255,255]
black = [0,0,0]

    
for i in np.arange(height):
    for j in np.arange(width):
        if outImg[i,j][0] != outImg[i,j][1] != outImg[i,j][2]:
            colored = 1
            break
    if colored == 1:
        break

if colored == 1:
    for i in np.arange(height):
        for j in np.arange(width):
            c = (int(outImg[i,j][0]) + int(outImg[i,j][1]) + int(outImg[i,j][2]))/3
            outImg[i,j] = [int(c), int(c), int(c)]
            
    

for i in np.arange(height):
    for j in np.arange(width):
        if  outImg[i,j][0] > threshold:
            outImg[i,j] = white
        else:
            outImg[i,j] = black

plt.imshow(outImg)
plt.title(newImg + '\nthreshold = ' + str(threshold))
Image.fromarray(outImg).save(newImg)
plt.show()