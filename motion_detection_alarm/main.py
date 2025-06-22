#import main class
from motion_detector import MotionDetector

#create and instance of the motion detection system and start
def main():
    detector = MotionDetector()
    detector.start()

#run the main function