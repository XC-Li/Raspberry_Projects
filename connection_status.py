import os
import time
from sakshat import SAKSHAT

SAKS = SAKSHAT()
led = SAKS.ledrow
buzzer = SAKS.buzzer
try:
    while True:
        time.sleep(2)
        ip_list = []
        raw_result = os.popen("netstat -nat | grep 'ESTABLISHED'")
        for line in raw_result:
            ip_port = (line[44:-17])
            ip = ip_port.split(":")[0]
            port = ip_port.split(":")[1]
            #print(type(ip))
            if ip not in ip_list:
                ip_list.append(ip)
            
        local_count = 0
        foreign_count = 0
        local = False
        foreign = False
        for ip in ip_list:    
            if ip.startswith("192.168"):
                local = True
                local_count = local_count + 1
            else:
                foreign = True
                foreign_count = foreign_count + 1
                
        print(local,local_count,foreign,foreign_count)
        led.off()
        if local == True:
            for i in range(0,local_count):
                #led.on_for_index(i)
                pass
        if foreign == True:
            #for i in range(7,7-foreign_count,-1):
            #    led.on_for_index(i)
            led.on_for_index(7)
          
except:
    led.off()
    buzzer.off()
