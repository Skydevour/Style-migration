#-*- coding:utf-8 -*- 
# @Time : 2021/2/22 11:27 
# @Author : 万志杨
# @File : pi.py 
# @Software: PyCharm

import cv2
import numpy as np
from PIL import Image

#读入图片：默认彩色图，cv2.IMREAD_GRAYSCALE灰度图，cv2.IMREAD_UNCHANGED包含alpha通道
img1 = cv2.imread('images/baby.jpg')
img2 = cv2.imread('images/style.jpg')
img = cv2.imread('images/picasso.jpg')
p0=cv2.resize(img1,(1080,1080),interpolation=cv2.INTER_CUBIC)
p1=cv2.resize(img2,(1080,1080),interpolation=cv2.INTER_CUBIC)
# cv2.imshow('src',p1)
# print(p1.shape) # (h,w,c)
# print(p1.size) # 像素总数目
# print(p1.dtype)
# print(p1)
cv2.waitKey()


cv2.imwrite("images/boy.jpg", p0)
cv2.imwrite("images/girl.jpg", p1)

# im_array = np.array(p0)
# p0 = Image.fromarray(np.uint8(im_array))
# p0.save('baby1.jpg')
# p1.save('style1.jpg')



