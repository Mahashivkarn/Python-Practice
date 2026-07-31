class employee:
    
    def __init__(self,salary,name,bond):
        self.salary=salary
        self.name=name
        self.bond=bond
    
    def get_salary(self):
        return self.me
    
    def get_info(self):
        return (f"The salary is{self.salary} ,The name is {self.name} and the bond is of{self.bond}")
    
e1= employee(34500,"Jhon Wick",4)
# print(e1.get_salary())
print(e1.get_info())