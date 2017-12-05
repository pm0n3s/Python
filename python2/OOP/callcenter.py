from datetime import datetime
import time
now = datetime.now()

class Call(object):
    def __init__(self,uid,name,num,reason):
        self.id = uid
        self.name = name
        self.num = num
        self.reason = reason
        self.time = now
    def display(self):
        print "id:", self.id
        print "name:", self.name
        print "num:", self.num
        print "reason:", self.reason
        print "time:", self.time
        

class callCenter(object):
    def __init__(self):
        self.calls = []
        self.que = 0
    def add(self, call):
        self.calls.append(call)
        self.que += 1
        return self
    def remove(self, call):
        self.calls.remove(call)
        self.que -= 1
        return self
    def info(self):
        for i in range(0, len(self.calls)):
            print "name: {}, num: {}".format(self.calls[i].name, self.calls[i].num)
    def ninja(self, num):
        for i in range(0, len(self.calls)):
            if self.calls[i].num == num:
                self.calls.remove(self.calls[i])
                break
        return self
    def hacker(self):
        self.calls = sorted(self.calls)
        return self

caller1 = Call(1, "Pat", "555-123-4567", "Software") 
caller1.display()
caller2 = Call(2, "Shelby","555-123-9876", "Hardware") 
caller2.display()
callcenter1 = callCenter()
callcenter1.add(caller2).add(caller1).hacker().info()




