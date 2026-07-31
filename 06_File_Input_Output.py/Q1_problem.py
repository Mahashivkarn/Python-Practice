
f=open("poem.txt")

data=f.read()

if("Twinkle" in data):
    print("The Word Twinkle is present in data")
    
else:
    print("The Word Twinkle is not present in the data")
    
f.close()