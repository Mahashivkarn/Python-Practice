class Animal:
    
    def sound(self):
        print("Some Sound")
        
class Dog(Animal):
    
    def sound(self):
        print("Bark!")
        
a=Dog()
a.sound()