import numpy as np 
import cv2


img = cv2.imread("Resources/l1.jpg")

print('Original dimensions :', img.shape)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
width = int(img.shape[1] * 20 / 100)
he = int(img.shape[0] * 20 / 100)
dim = (width, he)


img2 = cv2.resize(imgGray,dim)
img2C = cv2.Canny(img2,100,200)





cv2.imshow("Gray Image",img2C)
cv2.waitKey(0)
cv2.destroyAllWindows()
print('closing')
