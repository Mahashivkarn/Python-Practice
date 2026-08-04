def marks(**kwargs):
    #Kwargs is an dictionary wit values passed to the marks
    for item in kwargs:
        print(f"The marks of {item} are {kwargs[item]}")
        
        
marks(Dhruv =9,Yash =7, Mohit =7.5,Arnav =8)