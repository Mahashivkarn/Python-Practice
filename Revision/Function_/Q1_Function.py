def calculate_area(length,width=3):
   area= length * width 
   return area  

length =int(input("Length:"))
a=calculate_area(length,width=3)
print(a)