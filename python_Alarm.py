# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 16:28:53 2024

@author: Anupam
"""

import datetime as dt
import time

class AlarmClock:
    def __init__(self, sound_time):
        # Initialize the alarm clock with a sound time
        self.__sound_time = dt.datetime.strptime(sound_time, "%H:%M")
        self.__current_time = None

    def __str__(self):
        # Return a string representation of the alarm clock
        return f"Alarm Clock set to {self.__sound_time.strftime('%H:%M')}"

    def get_current_time(self):
        # Get the current time
        self.__current_time = dt.datetime.now()
        return self.__current_time

    def ring(self):
        # Ring the alarm when the current time matches the sound time
        while True:
            self.get_current_time()
            if self.__current_time.hour == self.__sound_time.hour and self.__current_time.minute == self.__sound_time.minute:
                print("Alarm is ringing!")
                break
            # Wait for 1 second before checking again
            time.sleep(1)

# Create an instance of the AlarmClock class
alarm = AlarmClock("16:40")
print(alarm)  # Output: Alarm Clock set to 16:40
alarm.ring()