import cv2
import  numpy as np

# img = cv2.imread("C:\\Users\\duttam\\PycharmProjects\\Project_1\\Ex_Files_OpenCV_Python_Dev\\Exercise Files\\Ch03\\03_04 Begin\\faces.jpeg",1)
# r_image = cv2.resize(img,(0,0),fx=0.15,fy=0.15)
# #cv2.imshow("original image",img)
# hsv= cv2.cvtColor(r_image,cv2.COLOR_BGR2HSV)
# h = hsv[:,:,0]
# s = hsv[:,:,1]
# v = hsv[:,:,2]
#
# hsv_split = np.concatenate((h,s,v),axis=1)
# hsv_merge = cv2.bitwise_and(h,s)
# cv2.imshow("hsv split", hsv_split)
# cv2.imshow("hsv merge", hsv_merge)
# # cv2.imshow("resize image",hsv)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)
while (True):
    ret, frame = cap.read()
    frame = cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    cv2.imshow("Frame",frame)   
    ch = cv2.waitKey(1)
    if ch ==ord('q'):
            break

cap.release()
cv2.distroyAllWindows()
# height , width, channel = img.shape
# b, g, r  = cv2.split(img)
# combined_image = np.empty([height,width*3,3],'uint8')
# combined_image[:,0:width] = cv2.merge([b,g,r])
# combined_image[:,0:width]= cv2.merge([b,b,b])
# combined_image[:,width:width*2] = cv2.merge([g,g,g])
# combined_image[:,width*2:width*3] = cv2.merge([r,r,r])
# cv2.imshow("Image",combined_image)
# cv2.waitKey(0)
# cv2.distroyAllWindows()
#
