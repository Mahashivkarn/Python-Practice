class Person:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def call(self):
        print(self.name,self.age)
        
a=Person("Dhruv",20)

a.call()