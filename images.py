import numpy as np
import cv2

boundaries = [
	([17, 15, 100], [50, 56, 200]),
	([86, 31, 4], [220, 88, 50]),
	([25, 146, 190], [62, 174, 250]),
	([103, 86, 65], [145, 133, 128])
]
image = cv2.imread("Resources/l1.jpg")
width = int(image.shape[1] * 10 / 100)
he = int(image.shape[0] * 10 / 100)
dim = (width, he)
print('Original dimensions :', image.shape)
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
output2 = cv2.resize(output, dim)
cv2.imshow("red in image", output2)
	# show the images
	# cv2.imshow("images", np.hstack([image, output]))
    # imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #
    #
    # img2 = cv2.resize(img,dim)
    # img2C = cv2.Canny(img2,100,400)

cv2.waitKey(0)
cv2.destroyAllWindows()
print('closing')
