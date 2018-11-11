import  cv2
import  numpy as np



road_image = cv2.imread('C:\\Users\\duttam\\Downloads\\road.jpg',1)
car_image = cv2.imread('C:\\Users\\duttam\\Downloads\\car.jpg',1)

gray_car = cv2.cvtColor(car_image, cv2.COLOR_BGR2GRAY)
_,mask = cv2.threshold(gray_car, 240,255,cv2.THRESH_BINARY)
inv_mask = cv2.bitwise_not(mask)

fg_image = cv2.bitwise_and(car_image,car_image,mask= inv_mask)
bg_image = cv2.bitwise_and(road_image,road_image,mask=mask)
final_image = cv2.add(fg_image,bg_image)
# cv2.imshow('Road image',road_image)
# cv2.imshow('Car Image',car_image)
# cv2.imshow('mask Image',mask)
# cv2.imshow('inv mask',inv_mask)
cv2.imshow('fore ground',fg_image)
cv2.imshow('back ground',bg_image)
cv2.imshow('Final_Image',final_image)


cv2.waitKey(0)
cv2.destroyAllWindows()