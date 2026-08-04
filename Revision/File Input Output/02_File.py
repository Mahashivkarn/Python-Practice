# Write a file called Jhon Doe.txt
#It should contain the info. about Jhon Doe.

f = open("Jhon Doe.txt","w")

l='''
  Jhon Doe is An Enterprenapur/Start-up Founder 
  Just at The age of 21.
  He is also a great Volleyball Player.
'''

f.write(l)

f.close()
