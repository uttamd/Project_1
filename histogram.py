import  cv2
import  numpy as np
from  matplotlib import pyplot as plt

img = np.zeros((500,500),np.uint8)

cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()