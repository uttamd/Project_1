import cv2 as cv2
import  numpy as np

cap = cv2.VideoCapture(0)
def fun(X):
    pass

cv2.namedWindow("frame")
cv2.createTrackbar("test","frame",50,500,fun)
while True:
    _, frame = cap.read()

    test = cv2.getTrackbarPos("test","frame")
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frame, str(test), (50, 150), font, 4, (0, 0, 255))
    cv2.imshow('frame', frame)
    a = cv2.waitKey(1)
    if a == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
