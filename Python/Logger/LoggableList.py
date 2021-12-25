from Loggable import Loggable

class LoggableList(list, Loggable):
    def append(self, item):
        super().append(item)
        super().log(item)

a = LoggableList()
a.append('msg 1')
a.append('msg 2')
print(a)