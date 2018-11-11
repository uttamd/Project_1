import numpy as np
import cv2


img = cv2.imread("C:\\Users\\duttam\\PycharmProjects\\Project_1\\Ex_Files_OpenCV_Python_Dev\\Exercise Files\\Ch02\\02_04 Begin\\butterfly.jpg",1)
#cv2.imshow("Image",img)
height, widhth, channel = img.shape
#print(height, widhth, channel)
b,g,r= cv2.split(img)
large_image = np.empty([height, widhth*3,3])
large_image[:,0:widhth] = cv2.merge((0,b,0))
large_image[:,widhth:widhth*2] = cv2.merge((g,g,g))
large_image[:,widhth*2:widhth*3]=  cv2.merge((r,r,r))

cv2.imshow("image",large_image)
cv2.waitKey(0)

