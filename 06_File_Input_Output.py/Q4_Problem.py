words ="Donkey"


with open("files.txt","r") as f:
    content =f.read()
     
    new =content.replace(words,"######")

with open("files.txt","w") as f:
    f.write(new)