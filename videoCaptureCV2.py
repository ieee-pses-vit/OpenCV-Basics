import numpy as np
import cv2 as cv

cam=cv.VideoCapture('SampleVideo_640x360_10mb.mp4')
cam.set(cv.CAP_PROP_FRAME_WIDTH,300)
cam.set(cv.CAP_PROP_FRAME_HEIGHT,300)

print(cam.get(cv.CAP_PROP_FRAME_WIDTH))
print(cam.get(cv.CAP_PROP_FRAME_HEIGHT))
if not cam.isOpened():
    print("Cannot Open Camera")
    exit()
while True:
    ret,frame=cam.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    #gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cv.imshow('frame',frame)
    if cv.waitKey(1)==ord('q'):
        break
cam.release()
cv.destroyAllWindows()
    
