from time import ctime
from time import sleep
from sakshat import SAKSHAT
from sakspins import SAKSPins as Pins

saks = SAKSHAT()
alarm = [2011]

def tact_event_handler(pin, status):
    global alarm_run
    if pin == Pins.TACT_RIGHT:
        print("Stop timer")
        alarm_run = False

try:
    while True:
        current_time = ctime()
        current_time = current_time[11:13] + current_time[14:16]
        print(current_time)
        if int(current_time) in alarm:
            saks.buzzer.beep(1)
        sleep(2)

except KeyboardInterrupt:
    print("End")
    saks.ledrow.off()
    saks.buzzer.off()