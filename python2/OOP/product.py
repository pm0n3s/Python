class Product(object):
    def __init__(self,price,name,weight,brand):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    def sell(self):
        self.status = "sold"
        return self
    def add_tax(self, tax):
        self.tax = tax
        tax_ammount = self.price * (1.0 + self.tax)
        return tax_ammount
    def Return(self, reason):
        self.reason = reason
        if self.reason == "defective":
            self.status = "defective"
            self.price = 0
        elif self.reason == "in box: like new":
            self.status = "for sale"
        elif self.reason == "in box: opened":
            self.status = "used"
            self.price = self.price * 0.8
        return self
    def display_info(self):
        print "Price: $",  str(self.price)
        print "Name:",     str(self.name)
        print "Weight:",   str(self.weight), "lbs"
        print "Brand:",    str(self.brand)
        print "Status:"    str(self.status)

