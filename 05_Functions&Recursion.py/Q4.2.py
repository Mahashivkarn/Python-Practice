def sum_of_digits(n):
    if(n==0):
        return 0
    else:
        return n + sum_of_digits(n-1)
    
print(sum_of_digits(5))