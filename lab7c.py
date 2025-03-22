#!/usr/bin/env python3

class Time:
    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def valid_time(t):
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True

def time_to_sec(time):
    return time.hour * 3600 + time.minute * 60 + time.second

def sec_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def sum_times(t1, t2):
    return sec_to_time(time_to_sec(t1) + time_to_sec(t2))

def change_time(time, seconds):
    total = time_to_sec(time) + seconds
    nt = sec_to_time(total)
    time.hour = nt.hour
    time.minute = nt.minute
    time.second = nt.second
