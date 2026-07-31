def convtemp(cel):
    f=(cel*(9/5))+32
    print(f"{cel} in celcius is {f} in fahrenheit")
    print("Thank You")
    
cel=int(input("Enter tem in celcius:"))
convtemp(cel)