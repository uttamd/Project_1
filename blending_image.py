import  cv2
import  numpy as np

road_image = cv2.imread('C:\\Users\\duttam\\Downloads\\road.jpg',1)
car_image = cv2.imread('C:\\Users\\duttam\\Downloads\\car.jpg',1)

gray_car = cv2.cvtColor(car_image, cv2.COLOR_BGR2GRAY)
_,mask = cv2.threshold(gray_car,245,255,cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img_bg = cv2.bitwise_and(road_image,road_image,mask=mask)
img_fg = cv2.bitwise_and(car_image,car_image,mask=mask_inv)
dst = cv2.add(img_bg,img_fg)

# cv2.imshow("road",road_image)
# cv2.imshow("car",car_image)
cv2.imshow("mask",mask)
cv2.imshow("inverse mask",mask_inv)
cv2.imshow("road img mask",img_bg)
cv2.imshow("car img invere",img_fg)
# cv2.imshow("image final",dst)

cv2.waitKey(0)
cv2.destroyAllWindow()
