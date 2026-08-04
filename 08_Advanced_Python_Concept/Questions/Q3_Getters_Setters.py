class employee:
    def __init__(self,salary):
        self._salary=salary
        
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self,value):
        if(value<0):
            print("Hey please dont set negative values")
        else:
            self._salary =value
    
e=employee(40000)
e.salary=9999
print(e.salary)