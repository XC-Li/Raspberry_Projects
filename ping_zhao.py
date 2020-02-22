# Check Zhao's status
import os
import time


class Device(object):
    def __init__(self, name, ip):
        self.device_name = name
        self.device_ip = ip
        self.last_online = "N/A"
        self.last_offline = "N/A"
        self.current_status = self._ping_ip()
        self.previous_status = self._ping_ip()
        if self.previous_status:
            self.last_online = time.ctime()
        else:
            self.last_offline = time.ctime()

    def _ping_ip(self):  # helper function
        r = os.popen("ping " + self.device_ip + " -c 1").readlines()
        for l in r:
            if l.find("Unreachable") != -1:  # or l.find("0 received") != -1:
                return False
        return True

    def _write_record(self,record):
        with open("zhao_rec.txt", "a") as file:
            file.write(record)

    def check_status(self):
        current_time = time.ctime()
        self.current_status = self._ping_ip()
        if self.previous_status is False and self.current_status is True:
            # device online
            self.last_online = current_time
            self._write_record(str(self.device_name + " Online: " + current_time + "\n"))
        if self.previous_status is True and self.current_status is False:
            # device offline
            self.last_offline = current_time
            self._write_record(str(self.device_name + " Offline: " + current_time + "\n"))

        self.previous_status = self.current_status


devices = [Device("mobile", "192.168.1.156"), Device("pc", "192.168.1.158")]
try:
    while True:
        if int(time.ctime()[14:-8]) % 10 == 0:
        # if True:
            print("Checking...")
            for device in devices:
                device.check_status()
            time.sleep(60)
        else:
            print("Waiting...")
            time.sleep(1)
        os.system("clear")
        print(time.ctime())
        for device in devices:
            print(device.device_name, "current:", device.current_status,
                  "online:", device.last_online, "offline:", device.last_offline)
except KeyboardInterrupt:
    print("Exit")

