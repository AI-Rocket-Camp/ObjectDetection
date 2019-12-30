#!-*-coding:UTF8-*-

import cv2

img = cv2.imread('ywk.png')

# 1.获取像素的值
px = img[200, 180]
print(px)  # [21 31 48]

# 只获取蓝色blue通道的值,0,蓝色；1，绿色；2，红色
px_blue = img[100, 90, 0]
print(px_blue)  # 103


# 2.修改像素的值
img[100, 90] = [255, 255, 255]
print(img[100, 90])  # [255 255 255]


# 3.图片形状
print(img.shape)  # (1000, 750, 3)
# 形状中包括行数、列数和通道数
height, width, channels = img.shape
# img是灰度图的话：height, width = img.shape

# 总像素数
print(img.size)  # 263*247*3=194883
# 数据类型
print(img.dtype)  # uint8


# 4.ROI截取
face = img[100:300, 205:408]
cv2.imshow('face', face)
cv2.waitKey(0)


# 5.通道分割与合并
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))
# 更推荐的获取某一通道方式
b = img[:, :, 0]
cv2.imshow('b', b)
cv2.waitKey(0)
