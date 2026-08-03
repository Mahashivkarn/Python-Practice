def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

@repeat(7)
def say_hello(a):#This function is wrapped with @repeat(7) so it looks like 
    print(f"Hello {a}!")
    '''
def wrapper(a):
    for i in range(7):
        say_hello(Dhruv)
    '''
    
say_hello("Dhruv")