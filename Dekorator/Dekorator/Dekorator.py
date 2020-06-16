
def my_decorator(func):
    def wrapper():
        print("before Advice")
        func()
        print("After Returning Advice")
    return wrapper


@my_decorator
def say_muh():
    print("Muh")


#say_muh = my_decorator(say_muh)

say_muh()


def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("log it")
        retval = func(*args, **kwargs)
        print("after log")
        return retval
    return wrapper

@log_decorator
def add(a,b):
   return a + b

@log_decorator
def sub(a,b):
    return a - b

print(add(3,4))

