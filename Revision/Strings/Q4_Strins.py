s ="Coding in Python is fun" 

sum=0
vowels =['a','e','i','o','u']

for char in s.lower:
    if(char in vowels):
        sum+=1
        
print(sum)