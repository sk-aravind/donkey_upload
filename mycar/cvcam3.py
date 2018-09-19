import cv2
import time

class CvCam(object):

	def __init__(self):
		self.cap = cv2.VideoCapture(0)
		self.frame = None

	def run(self):
		ret, self.frame = self.cap.read()
		return self.frame