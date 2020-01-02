#!-*-coding:UTF8-*-


import cv2
import numpy as np

img = cv2.imread('lena.jpg')
img=cv2.resize(img,(300,360))


# 高斯滤波不同参数对比
gau_blur3 = cv2.GaussianBlur(img, (3, 3), 0)
gau_blur5 = cv2.GaussianBlur(img, (5, 5), 0)
gau_blur9 = cv2.GaussianBlur(img, (9, 9), 0)

# 三张图片横向叠加对比显示
res = np.hstack((gau_blur3, gau_blur5, gau_blur9))
cv2.imshow('gau-compare', res)
cv2.waitKey(0)