"""import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img=cv.imread('image1.jpg',0)
print(img.shape)
height,width=img.shape[:2]
#cv.resize for rescaling
res=cv.resize(img,(int(0.5*width),int(0.5*height)),interpolation=cv.INTER_LINEAR)
print(res.shape)
cv.imshow('img',res)
#Number of Coloumns= Width
#Number of Rows=Height
#cv.warpAffine for translation
rows,cols=img.shape
M=np.float32([[1,0,100],[0,1,100]])
dst=cv.warpAffine(img,M,(cols,rows))
cv.imshow('img2',dst)
#cv.getRotationMatrix2D() for rotating images
M=cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),180,1)
dsst=cv.warpAffine(img,M,(cols,rows))
cv.imshow('img3',dsst)
#cv.getAffineTransform()
pts1=np.float32([[50,50],[200,50],[50,200]])
pts2=np.float32([[10,100],[200,50],[100,250]])
M=cv.getAffineTransform(pts1,pts2)
dst=cv.warpAffine(img,M,(cols,rows))
plt.subplot(121),plt.imshow(img)
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()"""
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Image Thresholding
"""import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=plt.imread('image1.jpg')
ret,thresh1=cv.threshold(img,200,255,cv.THRESH_BINARY)
ret,thresh2=cv.threshold(img,200,255,cv.THRESH_BINARY_INV)
ret,thresh3=cv.threshold(img,200,255,cv.THRESH_TRUNC)
ret,thresh4=cv.threshold(img,200,255,cv.THRESH_TOZERO)
ret,thresh5=cv.threshold(img,200,255,cv.THRESH_TOZERO_INV)

titles=['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images=[img,thresh1,thresh2,thresh3,thresh4,thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
"""
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#2d CONVOLUTION
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img=plt.imread("image1.jpg")
kernel=np.ones((5,5),np.float32)/25
dst=cv.filter2D(img,-1,kernel)
blur=cv.blur(img,(5,5))#blur
gaussianBlur=cv.GaussianBlur(img,(5,5),0) #Gaussian Blur
median=cv.medianBlur(img,5)
bilateral=cv.bilateralFilter(img,9,75,75)

plt.subplot(231),plt.imshow(img),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(232),plt.imshow(dst),plt.title('2DFilter')
plt.xticks([]),plt.yticks([])
plt.subplot(233),plt.imshow(blur),plt.title('Averaging')
plt.xticks([]),plt.yticks([])
plt.subplot(234),plt.imshow(gaussianBlur),plt.title('Gaussian Blur')
plt.xticks([]),plt.yticks([])
plt.subplot(235),plt.imshow(median),plt.title('Median Blur')
plt.xticks([]),plt.yticks([])
plt.subplot(236),plt.imshow(bilateral),plt.title('Bilateral Filtering')
plt.xticks([]),plt.yticks([])
            

plt.show()
