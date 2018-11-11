import  numpy as np
import cv2

img = cv2.imread("C:\\Users\\duttam\\PycharmProjects\\Project_1\\Ex_Files_OpenCV_Python_Dev\\Exercise Files\\Ch02\\02_04 Begin\\butterfly.jpg",1)
# cv2.namedWindow("Image",cv2.WINDOW_AUTOSIZE)
# cv2.imshow("Image",img)
# print(img.shape)
# cv2.waitKey(0)
print(img.shape)
print(len(img[0]))
print(len(img))
print(img[0][0][0])
print(img[1,2,:])
