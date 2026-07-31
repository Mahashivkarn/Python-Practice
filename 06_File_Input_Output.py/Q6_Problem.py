with open("log.txt") as f:
    s=f.read()
    
if("python" in s):
    print("Yes")
    
else:
    print("Not present")