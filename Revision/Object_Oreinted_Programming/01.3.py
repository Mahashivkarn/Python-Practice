class animal:
    location = "Mathura"
    
    def __init__(self,name):
        self.name =name
        
    def call(self):
        print("Making genric sound")
        
class Dog(animal):
    def call(self):
        super().call()
        print("Woof")
        
class Cat(animal):
    def call(self):
        print("Meow")
        
d=Dog("Sheru")
d.call()
c=Cat("Pusu")
c.call()