import numpy as np
import  cv2

img = cv2.imread("C:\\Users\\duttam\\Downloads\\lane_lines.jpg",1)
img = cv2.resize(img,None,fx=.3,fy=.3,interpolation= cv2.INTER_AREA)


cv2.imshow("Image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()