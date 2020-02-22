from sakshat import SAKSHAT
import time
import random
import math

SAKS = SAKSHAT()
led = SAKS.ledrow
buzzer = SAKS.buzzer
digital = SAKS.digital_display
x = 0
try:
    while True:
    
        led.off()
        while random.random() > 0.5:
            led.on_for_index(int(math.floor(random.random()*8)))
            time.sleep(0.2)
        #digital.show("0"*(4-len(str(x)))+str(x))
        
        if x %100 == 0:
           # buzzer.beep(0.2)
            led.off()
            for i in range(9):
                led.on_for_index(i)
                time.sleep(0.1)
            for j in range(8):
                led.off_for_index(j)
                time.sleep(0.1)
        x = x + 1
except KeyboardInterrupt:
    led.off()
    digital.off()
    buzzer.off()
