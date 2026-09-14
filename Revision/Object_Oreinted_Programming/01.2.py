class eirgth:
    
    def __init__(self,name,role,marks):
        self.name=name
        self.role=role
        self.marks=marks
        
    def student_info(self):
        print(f"The name of student {self.name}, role is {self.role} and marks is {self.marks}")
        
    
s=eirgth("Dhruv","Multi_Talanted",88)

s.student_info()