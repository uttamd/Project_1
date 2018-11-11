import  numpy as np
import cv2

img = cv2.imread("C:\\Users\\duttam\\Downloads\\Ex_Files_OpenCV_Python_Dev\\Ex_Files_OpenCV_Python_Dev\\Exercise Files\\Ch02\\02_01 Begin\\opencv-logo.png",1)
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
cv2.imshow("Image",img)
cv2.waitKey(0)
# print('shape ',img.shape)
# print('size ',np.size(img))
# print(len(img[:,:0]))
# print('5th row 5th column',img[50][100])
# print(img)



