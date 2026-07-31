class employee:
    
    language="Pyhton" #This is an class attribute 
    salary="$40,00,000"
    
    def __init__(self,name,salary,language): #dundar method which is automatically called.
        self.name= name
        self.salary=salary
        self.language=language
        
        print("I am creating an object")
        
        
harry=employee("Harry",12000,"Java")    
print(harry.name,harry.salary,harry.language)  

