a=int(input("Enter a number: "))
b=int(input("Enter a number: "))

if b==0:
    raise ValueError("Plz don't divide by zero") #It gives a custom error.
print(f"Division is {a/b}")
        