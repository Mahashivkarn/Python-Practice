f=open("file.txt")
print(f.read)
f.close() 
# This same can be written by using with statement like this:
with open("file.txt") as f:
    print(f.read())
    
#no need for closing the file