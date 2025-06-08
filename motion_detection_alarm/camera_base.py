#import the OpenCV library for accessing the webcam and image processing
import cv2

class Camera:
    def __init__(self, width = 640, height = 480):
        #initialize the camera
        self._cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        #set the height and width of the video frame
        self._cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)

        self._cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    def read_frame(self):
    #read a single frame from the camera
        _, frame = self._cap.read()

        #return the captured frame
        return frame
    
#release the camera resource to free it for other application
#close all OpenCV windows that were opened