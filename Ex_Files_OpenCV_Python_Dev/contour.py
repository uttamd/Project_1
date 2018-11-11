import numpy as np
import cv2

img = cv2.imread("C:\\Users\\duttam\\PycharmProjects\\Project_1\\Ex_Files_OpenCV_Python_Dev\\Exercise Files\\Ch02\\02_04 Begin\\butterfly.jpg",1)

hsv= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
res, thre = cv2.threshold(hsv[:,:,0],25,255,cv2.THRESH_BINARY_INV)
cv2.imshow("original",img)
cv2.imshow("Thres",thre)
canny_img = cv2.Canny(img,1000,500)
cv2.imshow("canny images",canny_img)


cv2.waitKey(0)
cv2.destroyAllWindows()