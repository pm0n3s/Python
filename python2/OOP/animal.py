class Animal(object):
    def __init__(self, name, health):
        self.name   = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display(self):
        print "name:", self.name
        print "current health:", self.health
        return self

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name, health=150)
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name, health=170)
    def fly(self):
        self.health -= 10
        return self
    def display(self):
        Animal.display(self)
        print "i am a dragon"

anml = Animal('Jeff', 100)
anml.walk().walk().walk().run().run().display()

dog1 = Dog('Jerry')
dog1.walk().walk().walk().run().run().pet().display()

drgn = Dragon('Jamal')
drgn.display()