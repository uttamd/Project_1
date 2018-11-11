import  cv2
import numpy as np

img = cv2.imread('C:\\Users\\duttam\\Downloads\\balls.jpg',1)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, mask = cv2.threshold(gray_img,240,255,cv2.THRESH_BINARY_INV)

kernal = np.ones((5,5),np.uint8)
erosion = cv2.erode(mask, kernal,iterations= 3)
#cv2.imshow("Balls",img)
#cv2.imshow("gray ",gray_img)
cv2.imshow("mask ",mask)
cv2.imshow("erosion",erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()