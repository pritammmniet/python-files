'''In Python, a decorator is a function that can modify the behavior of another function or class.
 Decorators are a powerful feature of Python that allow you to modify the behavior of functions or
  classes without modifying the source code directly.

A decorator is a function that takes another function as an argument, and returns a new function
that usually adds some additional functionality to the original function. This is done by wrapping
the original function in another function, which can add new features before or after the original
function is called.----chatgpt'''
'''yeh tb jaroori hota jb aap orginal function /class  ko access na kr paao phir bhi aap chahte ho ki wah 
function/class kuch extra functionality rakhe mtlb wahi aap usse modify karne ka haq na rakhte ho'''

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper
def say_hi():
    return 'hello there'

decorate = uppercase_decorator(say_hi)
print(decorate())
#upar k do line aise bhi likh skte hai actually mein yahi hota hai
say_hi = uppercase_decorator(say_hi)
print(say_hi())

#baar baar aisa kaun likhega ...isko simple rakhne ka ek tarika hain
@uppercase_decorator
def say_hi():
    return "hello there"
print(say_hi())





#abb aap ek hi function pr multiple decorator apply kar skte hai bs order ka dhyan rakho wah bottom to up
#hota hai
def split_decorator(function):
    def wrapper():
        return function().split()
    return wrapper
#now
@split_decorator
@uppercase_decorator
def  say_hi():
    return "hello there"
print(say_hi())





#Accepting Arguments in Decorator Functions
def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        '''abb sawal yeh hai ki yahi wrapper_accepting_arguments hi kyun responsible hai to take the
        :argument ...dekho abb reason :-
        cities=decorator_with_arguments(cities) hi ho rha hai n under the hood ...aur agle hi line me hum
        yeh kar rahe hai
        cities("Nairobi","Accra") toh yahan dhyan cities kuch nahi hai balki abbb wah wahi wrapper_accepting
        _arguments hain ...toh function aliasing ka rule yaad karo ...if u are saying cities with 2 arguments
        =wrapper_accepting_arguments the this function should have two parameters to store them

        chat-gpt
        When the decorator is applied to the cities function using the @decorator_with_arguments syntax,
        the cities function is replaced with the wrapper_accepting_arguments function. This means that
        when you call cities("Nairobi", "Accra"), you are actually invoking the wrapper_accepting_arguments
         function.'''

        print("My arguments are: {0}, {1}".format(arg1,arg2))
        function(arg1, arg2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))

cities("Nairobi", "Accra")

#ek aur anokha tarika to pass the argument in dec
def decorator(msg):
    def inner_1(function):
        def inner_2():
            print(f"The table of 2 is given below:-")
            function()
            print(msg)
        return inner_2
    return inner_1
def fun1():
    for i in range(1,11):
        print(f"2 x {i} = {2*i}")
#1st method to use decorator
#fun1=decorator("Thank You!")(fun1)
#fun1()

#2nd method to use decorator
@decorator("Thank You!")
def fun1():
    for i in range(1,11):
        print(f"2 x {i} = {2*i}")
fun1()



