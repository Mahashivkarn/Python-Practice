while True:
    try:
        a=int(input("Enter a number: "))
        b=int(input("Enter a number: "))
                
        print(f"Division is {a/b}")
        
    except ZeroDivisionError:
        print("Don't divide by zero")
    except ValueError:
        print("Please don't enter words")
    except:
        print("Error Occured")