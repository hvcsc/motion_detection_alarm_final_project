#import OpenCV
import cv2

#abstract base class for motion detection
class BaseMotionDetector:
    def detect(self, current_frame, reference_frame):
        #abstract methods to be overridden
        raise NotImplementedError("This method should be overridden.")

#concrete implementation using basic frame differencing
