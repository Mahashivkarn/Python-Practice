password = "qwe123"
enter_pass=input("Enter Passwprd: ")

while(enter_pass != password):
    enter_pass=input("Wrong Password! Try Again.")#this will take the input again and again until u write Right password.One advantage of Infintite loop
    
print("Sucessfully Logged in")
