import  cv2
import  numpy as np




bg = np.ones((500,500,3),np.uint8)
bg[:,:] = (255,255,255)
#circle = cv2.circle(bg,(250,250),100,color,-1)
#bitwise_img = cv2.bitwise_or(bg,circle)
#cv2.imshow("circle",circle)
height, width, channel = bg.shape
#text = "Hello India"
font = cv2.FONT_HERSHEY_COMPLEX
color= (255,0,0)
#cv2.putText(bg, text, (10, 500), font, 4, (255, 0, 0), 2, cv2.LINE_AA)
#t= cv2.putText(bg, 'Hello India', (10, 500), font,4,color)
rectnagle = cv2.rectangle(bg,(10,10),(100,100), color,-1)
cv2.imshow("rectangle",rectnagle)

#cv2.imshow("bitwise",bitwise_img)


cv2.waitKey(0)
cv2.destroyAllWindows()