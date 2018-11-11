import cv2
import  numpy as np


cap = cv2.VideoCapture(0)

while True:

    _, frame = cap.read()
    gray_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gray_frame, 100,0.2,10)

    if corners is not  None:
        corners = np.int0(corners)
        for corner in corners:
            x,y = np.ravel(corner)
            cv2.circle(frame, (x,y),3,(0,0,255),-1)
    cv2.imshow("frame",frame)
    a= cv2.waitKey(1)
    if a == ord('q'):
        break

cap.release()
cap.destroyAllWindows()