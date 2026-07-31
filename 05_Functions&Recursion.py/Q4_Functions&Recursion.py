def sumof(n):
    if(n==0):
        return 0
    return n + sumof(n-1)
    
n=int(input("Enter a number:"))
print(f"Sum of first {n} natural number is {sumof(n)}")