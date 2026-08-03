class employee():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    @property
    def get_name(self):
        l=self.name.split(" ")
        print(l)
        return l[0]
    
    @get_name.setter
    def get_name(self,first):
        l =self.name.split(" ")
        new_name=f"{first} {l[1]}"#here we are changing the fistr name and adding the same surname and then changing the whole sel.name from instructor to new one.
        self.name=new_name
        
    
e=employee("Jack Repear",25)
# print(e.get_name())
# e.set_first_name("Dhruv")
# print(e.name)

print(e.get_name)
e.get_name="Dhruv"
print(e.name)