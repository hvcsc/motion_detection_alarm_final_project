#import from previous files
from camera_base import Camera
from frame_processor import FrameProcessor

import cv2
import threading
import winsound

class MotionDetector:
    def __init__(self):
        #initiaize the variables
        self._camera = Camera()
        self._frame_processor = FrameProcessor()

        self._alarm_active = False
        self._alarm_mode = False
        self._alarm_counter = 0

        #read and preprocess the initial frame
#play beeping alarm
#triggers the alarm if not already active
#start the motion detection loop
#release camera and close all windows