def greatno(a,b,c):
    if(a>b and a>c):
        print(f"{a} is the greatest Number")
    elif(b>a and b>c):
        print(f"{b} is the greatest Number")
    else:
        print(f"{c} is the greatest Number")
    print("Thank You")
    
a=int(input("Enter number a:"))
b=int(input("Enter number b:"))
c=int(input("Enter number c:"))

greatno(a,b,c)