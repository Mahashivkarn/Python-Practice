class employee:
    company="Dell" #This is Class Attribute.
    def __init__(self,salary,name,bond,company):
        self.salary=salary#This creates an instance/object attribute
        self.name=name
        self.bond=bond
        self.company=company
    
    def get_salary(self):
        return self.me
    
    def get_info(self):
        return (f"The salary is{self.salary} ,The name is {self.name} and the bond is of{self.bond}")
    
e1= employee(34500,"Jhon Wick",4,"Asus")
# print(e1.get_salary())
print(e1.company) #It will always print Instance attribute if present otherwise it will print class attribute.
print(employee.company) #This will always print CLass Atrribute.
#object introspection
print(dir(e1))
