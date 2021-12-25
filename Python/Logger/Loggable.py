import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))