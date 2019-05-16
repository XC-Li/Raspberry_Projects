#!/usr/bin/python3.5

# Sit timer to avoid sit for to long

# import packages
from sakshat import SAKSHAT
from sakspins import SAKSPins as Pins
import math
import sys
import time
import os

if len(sys.argv) == 2:
    try:
        TIME_LENGTH = int(sys.argv[1])
        print("Set time length to", TIME_LENGTH)
    except ValueError:
        print("Wrong time input! Only integer is accepted ")
        print("Please specify how many minute you want to work in integer format")
        exit(1)
else:
    print ("Wrong time input! Only one input is accepted ")
    print("Please specify how many minute you want to work in integer format")
    exit(1)

saks = SAKSHAT()

timer_run = False  # whether the timer is running
timer_end = False  # whether this time period has expired
timer_extend = False  # whether extend the time


# push down switch
def tact_event_handler(pin, status):

    global timer_run
    global timer_end
    global timer_extend
    if pin == Pins.TACT_RIGHT:
        print("Stop timer")
        timer_run = False
        timer_extend = False
        timer_end = False
    if pin == Pins.TACT_LEFT:
        print("Start timer")
        timer_run = True
        if timer_end:
            timer_extend = True


# led function
def led_indicator(arg):
    saks.ledrow.off()
    if 0 <= arg <= 7:
        saks.ledrow.on_for_index(7 - arg)


# extend the time and beep every ten minuets, called by timer function
def extend_time():
    extension_time = 0
    global timer_run
    while timer_run:
        time.sleep(0.5)
        saks.ledrow.off_for_index(7)
        time.sleep(0.5)
        saks.ledrow.on_for_index(7)
        extension_time += 1
        minute = extension_time // 60
        second = extension_time % 60
        os.system("clear")
        print("Extend Time:", minute, "minute", second, "second")
        if minute % 10 == 0 and second == 0:
            saks.ledrow.on_for_index(minute // 10 - 1)
            print("Beep!")
            saks.buzzer.beepAction(0.05, 0.45, 5)
            time.sleep(1)
            saks.buzzer.beepAction(0.3, 0.5, minute // 10)


# timer function
def timer(time_length):
    global timer_run
    global timer_end
    remain_time = 60 * time_length
    while timer_run:
        time.sleep(1)
        remain_time -= 1
        minute = remain_time // 60
        second = remain_time % 60
        progress_value = math.floor(remain_time / (60*time_length) * 8)
        # print(progress_value)
        led_indicator(progress_value)
        os.system("clear")
        print("Remaining:", minute, "minute and", second, "second")
        if remain_time <= 0:
            break

    if timer_run:
        timer_end = True  # set the flag timer_end to true, press left button again will cause extend time
        i = 0
        while True:
            print("Beep")
            saks.buzzer.beepAction(0.1, 0.9, 10)
            extend_time()
            if not timer_run:
                break
    else:
        print("Half way cancel")


#  main function
saks.tact_event_handler = tact_event_handler

print("Start")
# saks.buzzer.beep(2)
try:
    while True:
        time.sleep(2)
        os.system("clear")
        saks.ledrow.off()
        saks.buzzer.off()
        print("Waiting", time.ctime())
        if timer_run:
            timer(TIME_LENGTH)
        # feature: beep every 30 minute
        current_time = time.ctime()
        hour = int(current_time[11:13])
        minute = int(current_time[14:16])
        if hour > 9:
            if minute == 30:
                saks.buzzer.beepAction(0.1, 0.9, 2)
                time.sleep(60)
            if minute == 0:
                saks.buzzer.beepAction(0.1, 0.9, 5)
                time.sleep(60)
        
except KeyboardInterrupt:
    print("End")
    saks.ledrow.off()
    saks.buzzer.off()
