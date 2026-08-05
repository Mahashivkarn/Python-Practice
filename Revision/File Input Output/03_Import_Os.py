import os

a =os.listdir("dir")
print(a)

print(os.getcwd())
print(os.path.exists("harry"))#Tells us that the file exists or not.
# os.remove("dhruv.txt") for removing txt file
os.rmdir("dir")#It only delets empty directries.