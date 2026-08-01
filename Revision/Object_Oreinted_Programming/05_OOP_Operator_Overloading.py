class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def sum(self,p):
        return point(self.x +p.x,self.y+p.y)
    
    def print_point(self):
        return f"X is {self.x} and Y is {self.y}"
        
    def __add__(self,p):
        return point(self.x +p.x,self.y+p.y)
        
p1=point(5,4)
p2=point(2,3)

#p=p1.sum(p2)#returns a new point which is the sum of p1 and p2
p=p1+p2 #We overloaded the + operator by writing the __add__ method in the point class. Now we can use + operator to add two point objects.
print(p.print_point())