def greater(x):
    if x>9:
        return True
    else:
        return False
#We can also use lambda func. instead of this func, in so many lines like new =list(map(lambda x:x>9,l))
l= [22,234,31,12,2,3,1,234,542,324,21,1,4,56,7]
        
new = list(filter(greater,l))
print(new)