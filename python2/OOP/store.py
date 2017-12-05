class Store(object):
    def __init__(self, location, owner):
        self.location = location
        self.owner    = owner
        self.products = []
    def add_product(self, price, name, weight, brand):
        self.price   = price
        self.name    = name
        self.weight  = weight
        self.brand   = brand
        self.status  = "for sale"
        product_data = {
            "price"  : self.price,
            "name"   : self.name,
            "weight" : self.weight,
            "brand"  : self.brand,
            "status" : self.status
        }
        self.products.append(product_data)
        return self
    def remove_product(self, name):
        self.name = name
        for i in range(0,len(self.products)):
            for key, val in self.products[i].iteritems():
                if (key, val) == ("name", self.name):
                    del self.products[i]
        return self
    def inventory(self):
        if len(self.products) > 0:
            print "Name:",    str(self.name)
            print "Brand:",   str(self.brand)
            print "Price: $", str(self.price)
        else:
            print "no items in inventory"
        return self

store1 = Store("VA", "Pat")
store1.add_product(4.50, "Cherry Coke", 3, "Coca-Cola")
store1.inventory()
store1.remove_product("Cherry Coke")
store1.inventory()
