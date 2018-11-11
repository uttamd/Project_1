import numpy as np
import  cv2


car_image = cv2.imread('C:\\Users\\duttam\\Downloads\\car.jpg',1)
height, width, channel = car_image.shape

scaled_image = cv2.resize(car_image,None, fx=.5, fy= .5, interpolation= cv2.INTER_LINEAR)

matrix_t= np.float32([[1,0,50],[0,1,100]])
transform_image = cv2.warpAffine(car_image,matrix_t, (width, height))

matrix_r = cv2.getRotationMatrix2D((height/2,width/2),90,.5)
rotated_image = cv2.warpAffine(car_image, matrix_r,(width,height))

cv2.imshow("original image",car_image)
cv2.imshow("Resized Image",scaled_image)
cv2.imshow("Transform Image",transform_image)
cv2.imshow("Rotated Image",rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()