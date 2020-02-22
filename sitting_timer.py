import time

from sakshat import SAKSHAT
SAKS = SAKSHAT()
buzzer = SAKS.buzzer

buzzer.off()

def click(pin, status):
    print(pin)
    print(status)
    buzzer.beep(0.2)

SAKS.tact_event_handler = click
try:
    while True:
       time.sleep(1)
       print ("aa")
except KeyboardInterrupt:
    buzzer.off()

    