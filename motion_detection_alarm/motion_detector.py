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
        frame = self._camera.read_frame()
        self._reference_frame = self._frame_processor.preprocess(frame)

    #play beeping alarm
    def _play_alarm(self):
        for _ in range(3):
            if not self._alarm_mode:
                break
            print("ALARM")
            winsound.Beep(2500, 1000)
        self._alarm_active = False

    #triggers the alarm if not already active
    def _trigger_alarm(self):
        if not self._alarm_active:
            self._alarm_active = True
            threading.Thread(target = self._play_alarm, daemon = True).start()

    #start the motion detection loop
    #release camera and close all windows