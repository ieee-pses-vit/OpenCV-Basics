import cv2 as cv
import numpy as np
cap=cv.VideoCapture(0)
#while(1):
frame=cv.imread('msi_logo.jpg')
hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)

lower_red=np.array([0,50,50])
upper_red=np.array([5,255,255])

lower_green=np.array([50,50,50])
upper_green=np.array([70,255,255])

lower_blue=np.array([100,50,50])
upper_blue=np.array([120,255,255])

mask1=cv.inRange(hsv,lower_red,upper_red)
mask2=cv.inRange(hsv,lower_green,upper_green)
mask3=cv.inRange(hsv,lower_blue,upper_blue)
res1=cv.bitwise_or(mask1,mask2)
mask=cv.bitwise_or(mask3,res1)
res=cv.bitwise_and(frame,frame,mask=mask)
cv.imshow('frame',frame)
cv.imshow('mask',mask)
cv.imshow('res',res)
k = cv.waitKey(5) & 0xFF
#if k == 27:
    #break   

