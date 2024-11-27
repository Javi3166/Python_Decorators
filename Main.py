print("\nA decorator passes adds functionality to another function.")

def start_end_decorator(func):
    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper

def print_name():
    print('Emilio')

print("Normally to pass on functionality will involve equalling the previous to calling the other function with the"
      " initial one as an argument.")
# print_name = start_end_decorator(print_name())

print("\nHowever, it is possible to do it much more simply with the @ operator.")
@start_end_decorator
def print_name():
    print('Emilio')

print_name()

print("\nAs is, it won't be able to take arguments so when calling the wrapper and the function in the wrapper, "
      "\n'*args, **kwargs' must be put in the arguments list. They stand for arguments and keyword arguments."
      "\nThe results must also be returned in order to be able to show something.")

def start_end_decorator(func):
    def wrapper(*args, **kwargs):
        print('Start')
        wrap_result = func(*args, **kwargs)
        print('End')
        return wrap_result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

result = add5(10)
print(result)

print("\nHowever, like this it will hide the info of the add5() function and report the info of the wrapper instead in "
      "confusion.")

print(help(add5))
print(add5.__name__)

print("\nIn order to fix this, a tool from the functools module is needed.")
import functools

def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        wrap_result = func(*args, **kwargs)
        print('End')
        return wrap_result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

print(help(add5))
print(add5.__name__)

print("\nA default template for a decorator is the following:")
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do..
        wrap_result = func(*args, **kwargs)
        # Do...
        return wrap_result
    return wrapper

print("\nIt is possible to have the decorator be repeated.")
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for index in range(num_times):
                wrapper_result = func(*args, **kwargs)
            return wrapper_result
        return wrapper
    return decorator_repeat

@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")

greet('Alex')

print("\nIt is also possible to have nested decorators.")

def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        wrap_result = func(*args, **kwargs)
        print("End")
        return wrap_result
    return wrapper

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k} = {v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper

@debug
@start_end_decorator
def say_hello(name):
    greeting = f"Hello {name}"
    print(greeting)
    return greeting

say_hello('Emilio')

print("\nIt is also possible to make a decorator a subclass.")

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times.")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello")

say_hello()
say_hello()

print("\nThere are various possible uses of decorators. One of them include making a timer decorator that will "
      "\ncalculate the time of execution of a program. Another is the debug decorator to get more information about the "
      "\ncalled function and it's arguments. There is also the check decorator that can check arguments to see if they "
      "\nfulfill certain conditions and adapt accordingly. You can also register functions with decorators. You can also "
      "\ncash the return values or you can update the information or update the state.")