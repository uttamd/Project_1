import cv2
import  numpy as np

img = cv2.imread('C:\\Users\\duttam\\Downloads\\squares.jpg',1)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray_img,150,0.9,5)
if corners is not None:
    for corner in corners:
        corner = np.int0(corner)
        x,y = np.ravel(corner)
        cv2.circle(img,(x,y),3,(0,0,255),-1)
cv2.imshow("Suqare",img)
cv2.waitKey(0)
cv2.destroyAllWindows()