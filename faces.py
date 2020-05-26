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
	for (lower, upper) in boundaries:
		lower = np.array(lower, dtype = 'uint8')
		upper = np.array(upper, dtype = 'uint8')
		#mask to find colors within boundaries
		mask = cv2.inRange(frame,lower,upper)
		output = cv2.bitwise_and(frame, frame, mask = mask)
	cv2.imshow('frame', np.hstack([frame,output]))
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
