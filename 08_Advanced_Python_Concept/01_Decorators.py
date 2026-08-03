#Decorstor is a function that takes a function, it creates a new function inside its body (wrapper).Then it returns that new function.
def decorator(func):
    def wrapper():
        print("I am about to execute a function...") #this is the main thing when we say f=decorator(say_hello) that means we are passing the say_hello in the decorator fun. and the the wrapper fun works that prints I am about . line and our say_hello fun = fun() and then  I have executed the func. Line is printed .This is called nestedfunctions.
        func()
        print("I have executed the function...")
        
    return wrapper

@decorator

def say_hello():
    print("Hello!")
    
say_hello()
# f=decorator(say_hello)
# f() now by adding decorator it has become something like what we were trying to do with f =decoratora(say_hello) then F() not by the @ decorator it is no longer needed.