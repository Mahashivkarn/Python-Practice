def star(n):
    for i in  range(1,n+1):
        print("*"*(4-i),end="")
        print()
        
n =int(input("Enter a number:"))
print(f"pattern of {n} is:")
star(n)