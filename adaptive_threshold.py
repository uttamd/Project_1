import numpy as np
import cv2

img = cv2.imread("C:\\Users\\duttam\\PycharmProjects\\Project_1\\Ex_Files_OpenCV_Python_Dev\\Exercise Files\\Ch03\\03_03 Begin\\sudoku.png",0)
cv2.imshow("Original",img)

ret, thres_basic = cv2.threshold(img,70,255,cv2.THRESH_BINARY)
cv2.imshow("change image",thres_basic)

adaptive_thresh = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
cv2.imshow("Adaptive_Image",adaptive_thresh)



cv2.waitKey(0)
cv2.destroyAllWindows()