import numpy as np
import cv2






class TestClass:
	def __init__(self, realpart, imagpart):
		self.r = realpart
		self.i = imagpart 
	def f(self):
		return 'Welcome back'





x = TestClass(3,0.5)
img=cv2.imread('download.jpeg',0)
cv2.imshow('Road', img)
cv2.waitKey(0)
cv2.destroyAllWindows()




print('Program Closed! Saving...')
