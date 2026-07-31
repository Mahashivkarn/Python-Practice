class animal: #Parent Class (Superclass)
    location="Japan"
    def __init__(self,name):
        self.name =name
        
    def speak(self):
        print("Generic animal sound")
        
class dog(animal):#this will contain all the attributes of animal class
    def speak(self):
        super().speak() #we are using the speak function from parent class
        print("Woof!")
        
        
# a=animal("Dog")
# a.speak()

a=dog("bruno")
a.speak()
print(a.location)