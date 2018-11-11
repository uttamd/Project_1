import cv2
import  numpy as np

img = cv2.imread("C:\\Users\\duttam\\Downloads\\houghcircles2.jpg",1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30)

count = 0
for i in circles[0,:]:
     count +=1

print('circle count ',count)
cv2.waitKey(0)
cv2.destroyAllWindows()

