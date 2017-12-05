class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayinfo(self):
        print "price of bike:", str(self.price)
        print "max speed of bike:", str(self.max_speed)
        print "total miles:", str(self.miles)
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing"
        if self.miles >= 5:
            self.miles -= 5
        else:
            self.miles -= self.miles
        return self

Bike1 = Bike("$150", "20 MPH")
Bike1.ride().ride().ride().reverse().displayinfo()

Bike2 = Bike("$100", "15 MPH")
Bike2.ride().ride().reverse().reverse().displayinfo()

Bike3 = Bike("$10", "5 MPH")
Bike3.reverse().reverse().reverse().displayinfo()