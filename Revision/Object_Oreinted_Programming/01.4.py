class point:
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def sum(self,p):
        return point((self.x + p.x),(self.y + p.y))
    
    def prin_sum(self):
        return f"X = {self.x} , Y ={self.y}"
    
    def __add__(self,p):
        return point((self.x + p.x), (self.y+p.y))
    
a=point(3,4)
b=point(4,5)

# c=a.sum(b)

c=a+b #Now we overloaded the program by using add operand.
print(c.prin_sum())     