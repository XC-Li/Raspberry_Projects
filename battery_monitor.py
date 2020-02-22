# Keep Raspiberry from sudden power loss
# Designed By Xc.Li
# Mar.2018 

# Reference :http://www.raspberrypiwiki.com/index.php/Power_Pack_Pro

import sys
import time
import os
flag = 0
print "Battery Monitor start on Boot %s" %time.ctime()

def main_func(sleep_time,critical_battery,echo):
    
    global flag
    global lost_power_time
    
    battery_percent = os.popen("i2cget -y 1 0x62 0x4 b").readlines()[0].strip()
    battery_percent = int(battery_percent,0)
    
    if echo == True:
        print "Current Time: %s" % time.ctime()
        print "Battery:%5i%%" %battery_percent;
        
        # draw batery
        n = int(round(battery_percent / 10));
        print "----------- "
        sys.stdout.write('|')
        for i in range(0,n):
            sys.stdout.write('#')
        for i in range(0,10-n):
            sys.stdout.write(' ')
        sys.stdout.write('|+\n')
        print "----------- "
    
    if battery_percent == 100:
        if echo == True:
            print "Battery FULL"
        flag = 0
    if battery_percent < 100:           
        if flag == 0:
            lost_power_time = time.ctime()
            flag = 1
        if echo == True:
            print "Running on Battery"
            print "Lost power since:%s" %lost_power_time
    if battery_percent < 20:
        if echo == True:
            print "Battery LOW"  
    
	if battery_percent < critical_battery:
		print "System will shutdown in 60 seconds!:%s" %lost_power_time
                time.sleep(60)
		os.system("sudo shutdown")
        
    time.sleep(5)
    os.system("clear")
    
while 1:    
    main_func(5,10,True)        
