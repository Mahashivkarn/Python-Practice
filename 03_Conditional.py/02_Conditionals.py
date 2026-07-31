a =int(input("Enter Your Age:"))

if(a>=18):
    print("You Can Vote\n")
    print("You Can Drink\n")
    
elif(a<0):
    print("Invalid Age")
    
elif(a==0):
    print("Age Can not Be Zero")
    
else:
    print("You Are Still Minor\n")