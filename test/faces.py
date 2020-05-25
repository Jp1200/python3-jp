import numpy as np
import cv2






cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
while(True): 


	ret, frame = cap.read()


	cv2.imshow('frame', frame)
	if cv2.waitKey(20) & 0XFF == ord('q'):
		print('Program Closed! Saving...')
		break


cap.release()
cv2.destroyAllWindows()

# cv2 basic image read test from 05.20.2020
# img=cv2.imread('download.jpeg',0)
# cv2.imshow('Road', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




