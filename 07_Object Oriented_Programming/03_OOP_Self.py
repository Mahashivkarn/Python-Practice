class employee:
    
    class1="Elite" #This is an class attribute 
    salary="$40,00,000"
    
    def getinfo(self):
        print(f"The class is {self.class1}.The salary is {self.salary}")
        
    def greet(self):
        print("Good Morning")
        
harry=employee()
 #This is an object/instance attribute
harry.class1="Poor"
harry.getinfo() 