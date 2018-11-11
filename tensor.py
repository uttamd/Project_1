import numpy as np
import cv2

img = cv2.imread("C:\\Users\\duttam\\Downloads\\shapes_image.png",1)
#img = cv2.medianBlur(img,5)
gray = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
cv2.imshow('detected circles',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()