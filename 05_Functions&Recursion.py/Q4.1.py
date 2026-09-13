#Recursion 

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    '''
    for 1 = 1*0=1
    for 2:2*1=2 & 2*0=1
    fro 3:3*2=6 & 6*1=1
    for 4*3=12,12*2=24,4*1=1
    for 5: 5*4=20 & 20*3=60 & 60 *2=120 &60*1=1
    '''
    
    
print(factorial(5))