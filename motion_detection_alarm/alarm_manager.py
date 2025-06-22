#import threading and winsound
import threading
import winsound

class AlarmManager:
    #initialize variables
    def __init__(self):
        self._alarm_active = False
        self._alarm_mode = False

    #enable or disable alarm mode
    def toggle_alarm_mode(self):
        self._alarm_mode = not self._alarm_mode
        return self._alarm_mode

    #start the alarm sound if it's not already active
    def trigger_alarm(self):
        if not self._alarm_active:
            self._alarm_active = True
            threading.Thread(target = self._play_alarm, daemon = True).start()

    #play beeping sound unless turned off
    def _play_alarm(self):
        for _ in range(3):
            if not self._alarm_mode:
                break
            print("ALARM")
            winsound.Beep(2500, 1000)
        self._alarm_active = False

    #property to access the current alarm mode
    @property
    def alarm_mode(self):
        return self._alarm_mode 