#import threading and winsound
import threading
import winsound

class AlarmManager:
    #initialize variables
    def __init__(self):
        self._alarm_active = False
        self._alarm_mode = False
        
    #enable or disable alarm mode
    #start the alarm sound if it's not already active
    #play beeping sound unless turned off
    #property to access the current alarm mode