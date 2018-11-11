import  numpy as np
import cv2


car_image = cv2.imread('C:\\Users\\duttam\\Downloads\\car.jpg',1)
gray_car = cv2.cvtColor(car_image, cv2.COLOR_BGR2GRAY)
_, threshold = cv2.threshold(gray_car, 150,255,cv2.THRESH_BINARY)
im2, contours, hierarchy = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for i in contours:
    cv2.drawContours(threshold, i, -1, (0, 255, 0), 3)
    cv2.imshow("Car", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()