class employee():
    company ="HP"
                        #This whole is like a blueprint of a form where the form has name address age etc
    def salary(self): #here self is what is entered it becomes that for e=employee() self becomes e for e1 = employee() self becomes e1 .It changes accodrding to the call.
        return 12000
    
e = employee() #an object of class  employee is created here.
print(e.salary())#Employee salary is called.
                       #this whole is where u enter the detail in the blueprint like you name=Dhruv and then your address =Hidden leaf etc.
e1=employee()
print(e1.salary())
print(e1.company)