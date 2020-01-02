import cv2 as cv
import numpy as np
img = cv.imread('embrace.jpg')
cv.imshow('original',img)
cv.waitKey()

kernel = np.ones((5,5),np.uint8)
erosion = cv.erode(img,kernel,iterations = 1)
cv.imshow('erosion',erosion)
cv.waitKey()

dilation=cv.dilate(erosion,kernel,iterations=1)
cv.imshow('dilation',dilation)
cv.waitKey()

img = cv.imread('opening.png',0)
#img = cv.resize(img,(300,360))
opening=cv.morphologyEx(img,cv.MORPH_OPEN,kernel)
cv.imshow('img',img)
cv.waitKey()
cv.imshow('opening',opening)
cv.waitKey()

img = cv.imread('closing.png',0)
#img = cv.resize(img,(300,360))
closing=cv.morphologyEx(img,cv.MORPH_CLOSE,kernel)
cv.imshow('original',img)
cv.waitKey()
cv.imshow('closing',closing)
cv.waitKey()
cv.destroyAllWindows()