import numpy as np
import  cv2

def fun(x):
    pass
cap = cv2.VideoCapture(0)
cv2.namedWindow("Trackbars")

cv2.createTrackbar("L-H","Trackbars",0,179, fun)
cv2.createTrackbar("L-S","Trackbars",0,255, fun)
cv2.createTrackbar("L-V","Trackbars",0,255, fun)
cv2.createTrackbar("U-H","Trackbars",179,179, fun)
cv2.createTrackbar("U-S","Trackbars",255,255, fun)
cv2.createTrackbar("U-V","Trackbars",255,255, fun)

while True:
    _, frame = cap.read()
    hsv_img = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("L-H","Trackbars")
    l_s = cv2.getTrackbarPos("L-S", "Trackbars")
    l_v = cv2.getTrackbarPos("L-V", "Trackbars")
    u_h = cv2.getTrackbarPos("U-H", "Trackbars")
    u_s = cv2.getTrackbarPos("U-S", "Trackbars")
    u_v = cv2.getTrackbarPos("U-V", "Trackbars")
    lower_color = np.array([l_h,l_s,l_v])
    upper_color = np.array([u_h,u_s,u_v])
    mask = cv2.inRange(hsv_img,lower_color,upper_color)
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    a = cv2.waitKey(1)
    if a == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()