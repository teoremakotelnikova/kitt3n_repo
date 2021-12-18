def add_one(number):
    return number + 1

print(add_one(1))

def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f'Yo {name}, together we are the awesomest'

def greet_bob(greeter_func):
    return greeter_func('Bob')

print(greet_bob(say_hello))
print(greet_bob(be_awesome))

def parent():
    print("Prinrting from the parent() function")

    def first_child():
        print('Prinrting from the first_child() function')

    def second_child():
        print("Prinrting from the second_child() function")

    second_child()
    first_child()

parent()

def parent(num):
    def first_child():
        return 'Hi, I am Emma'

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child

first = parent(1)
second = parent(2)
print( first, second)

print(first(), '+', second())

def my_decoratos(func):
    def wrapper():
        print('SSomething is happening before the function is called')
        func()
        print('SSomething is happening after the function is called')
    return wrapper

def say_whee():
    print('Whee!')

say_whee = my_decoratos(say_whee)
say_whee()
print(say_whee)

from datetime import datetime
def not_during_the_night(func):
    def wrapper():
    #    if 7 <= datetime.now().hour < 22:
        if datetime.now().hour >= 23:
            func()
        else:
            pass
    return wrapper

def say_whee():
    print('Whee!')

say_whee = not_during_the_night(say_whee)

say_whee()

@my_decoratos
def say_whee():
    print('Whee!')

say_whee()

from decorators import do_twice
@do_twice
def say_whee():
    print('Whee!')

say_whee()

@do_twice
def greet(name):
    print(f'Hallo {name}')

greet('World')

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

hi_adam = return_greeting('Adam')
print(hi_adam)

print(print)
print(print.__name__)
#print(help(print))
print(say_whee)
print(say_whee.__name__)
