from datetime import datetime
import time
import os

class Clock:
    def __init__(self, alarm):
        self.alarm = alarm

    def check_alarm(self):
        while True:
            current_time = datetime.now()
            if current_time.hour == self.alarm.hour and current_time.minute == self.alarm.minute:
                print("Time to wake up!")
                break
            else: 
                print("Monitoring.....")
                time.sleep(15)

    def play_alarm(self):
        for _ in range(3):
            os.system("afplay /System/Library/Sounds/Glass.aiff")  
