'''Unlike class methods, which are decorated with @classmethod and take the class as the first
parameter, constructors are instance methods because they are bound to the instance of the class being
created. '''

'''The __init__ method is a reserved method in Python and has a predefined name, __init__, which stands 
for "initialize." It is executed automatically when an object of the class is created using the class name 
followed by parentheses, like a function call.'''
#1. default constructor is that which has  self only as parameter
#2. below code is for explaining parameterized constructor

'''class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Creating objects of the Rectangle class with different values
rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)

# Accessing object attributes
print(rect1.length)  # Output: 5
print(rect1.width)  # Output: 10

# Calling a method on the objects
print(rect1.area())  # Output: 50

print(rect2.length)  # Output: 3
print(rect2.width)  # Output: 7
print(rect2.area())  # Output: 21'''
'''In the example above, the Rectangle class has a parameterized constructor __init__ that takes 
two parameters, length and width, along with the self parameter. When creating objects of the Rectangle
 class, values for length and width are passed as arguments, which are then used to initialize the length
  and width attributes of the objects.

Note that the self parameter is automatically passed by Python and refers to the instance of
 the object being created. The values for length and width are passed explicitly when creating objects,
  and they are used to initialize the corresponding attributes of the objects inside the constructor.

Parameterized constructors are useful when you want to pass specific values to the constructor during
 object creation and use them to set the initial state of the objects. They provide flexibility and 
 customization in object initialization, allowing you to create objects with different values for different
  use cases.'''

#see an amazing stuff
class Car:
    def __init__(bro):#see here u can use any variable name in place of self
        bro.wife="sita"
        bro.brother="laxman"

ram1=Car()


'''In Python, unlike some other object-oriented programming languages, constructors do not have 
a return type'''
#it is also know as dunder method
