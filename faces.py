import numpy as np
import cv2



boundaries = [
	([17, 15, 100], [50, 56, 200]),
	([86, 31, 4], [220, 88, 50]),
	([25, 146, 190], [62, 174, 250]),
	([103, 86, 65], [145, 133, 128])
]


cap = cv2.VideoCapture(0)
while(True):
 	ret, frame = cap.read()

	cv2.imshow('WebCam', frame)
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
