a=float(input("Enter Marks of Maths:"))
b=float(input("Enter Marks of Physics:"))
c=float(input("Enter Marks of Chemistry:"))

total=(a+b+c)/300 * 100

if(a<0 or a>100):
    print("Invalid marks of Maths")
elif(b<0 or b>100):
    print("Invalid marks of Physics")
elif(c<0 or c>100):
    print("Invalid marks of Chemistry")
else:
    if(a<33):
        print("Student Failed in Maths")
    if(b<33):
        print("Student Failed In Physics")
    if(c<33):
        print("Student Failed In Chemistry")
    if(a>=33 and b>=33 and c>=33 and total>=40):
        print("Student Passed")
    else:
        print("Student Failed")
        
