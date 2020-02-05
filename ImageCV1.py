"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('paper1.png')
b,g,r = cv2.split(img)
img2 = cv2.merge([r,g,b])
plt.subplot(121);plt.imshow(img) # expects distorted color
plt.subplot(122);plt.imshow(img2) # expect true color
plt.show()

cv2.imshow('bgr image',img) # expects true color
cv2.imshow('rgb image',img2) # expects distorted color
cv2.waitKey(0)
cv2.destroyAllWindows()
++++++++++++++++++++++++++++++++++++
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img=cv.imread('paper1.png',0)
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.xticks([]),plt.yticks([])
plt.show()
++++++++++++++++++++++++++++++++++++
cv.imshow('Open Hand',img)
k=cv.waitKey(0) & 0xFF
if k==27:#wait for esc key to exit
    cv.destroyAllWindows()
elif k==ord('s'):#wait for 's' key to save and exit
    cv.imwrite('paper1gray.png',img)
    cv.destroyAllWindows()"""
import cv2 as cv
import numpy as np
from time import sleep
import matplotlib.pyplot as plt
img1=cv.imread('image1.jpg')
img2=cv.imread('image2.jpg')
img3=cv.imread('image3.jpg')
dst=cv.addWeighted(img1,0.6,img2,0.4,-1)
mst=cv.addWeighted(dst,0.6,img3,0.8,0)
cv.imshow('dst',mst)
cv.waitKey(0)
cv.destroyAllWindows()
#something=img[180:300,270:390]
#img[0:120,100:220]=something
#b,g,r=cv.split(img)
#img=cv.merge((b,g,r))
#cv.imshow('aryan',img)                                                                                                                                                
