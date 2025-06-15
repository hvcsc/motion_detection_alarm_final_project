#import OpenCV and imutils libraries
import cv2
import imutils

class FrameProcessor:
    def preprocess(self, frame):
        #resize the frame
        frame = imutils.resize(frame, width = 500)
        #convert the color frame to grayscale for easier processing
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #apply gaussian blur
        frame = cv2.GaussianBlur(frame, (5, 5), 0)

        #return processed frame
