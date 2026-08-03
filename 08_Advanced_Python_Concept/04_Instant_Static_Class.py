class employee():
    company = "Dell"
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    # instance method (DEfault)
    def print_info(self):
        print(f"The name of employee is {self.name} and age is {self.age}")
        
        
    @staticmethod
    def sum(a,b):
        return a+b
        
e1=employee("Rohan","25")
e2=employee("Hoor","27")
# print(employee.company)
# print(employee.name) #No we can can't print naem by this because name is an instance attribute and company is an class attribute.
e1.print_info()
e2.print_info()

print(e2.sum(5,23))#without the static method this will give error bcuz the fun doesnot contain self parameter .