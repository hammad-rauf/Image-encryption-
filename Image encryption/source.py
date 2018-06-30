from rsa import *
import numpy as np
import cv2 as cv
import ctypes

obj = rsa()


img = cv.imread("green.jpg",cv.IMREAD_COLOR)
height, width, channels = img.shape


temp = np.zeros((height,width,3), np.int64)
     
for a in range (0,height):
    for b in range (0,width):
            x,y,z =  img[a][b]
            x = np.int(x)
            y = np.int(y)
            z = np.int(z)
            x = obj.Cipher(x)
            y = obj.Cipher(y)
            z = obj.Cipher(z)
            temp[a][b] = x,y,z
cv.imshow("image",temp)
cv.waitKey(0)
cv.destroyAllWindows()          
  
temp1 = np.zeros((height,width,3), np.uint8)

for a in range (0,height):
    for b in range (0,width):
            x,y,z =  temp[a][b]
            x = np.int(x)
            y = np.int(y)
            z = np.int(z)
            x = obj.deCipher(x)
            y = obj.deCipher(y)
            z = obj.deCipher(z)
            x = np.uint8(x)
            y = np.uint8(y)
            z = np.uint8(z)
            temp1[a][b] = x,y,z
      
cv.imshow("image",temp1)
cv.waitKey(0)
cv.destroyAllWindows()