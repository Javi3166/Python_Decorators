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