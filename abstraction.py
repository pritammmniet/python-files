#kahani by me :-
''' dekho, baat yeh hai ki abstract class ka yeh fayda hota hai ki hum abstract class ke abstract methods
 ko dekh ke yeh keh skte hai ki jitne bhi iske subclass hai wah saare me yeh abstract methods ka
 implementions hua hai wah aise ki maano agr ek subclass mein tumne abstract class ka implemention nahi kara
 toh kya hoga??
 toh error aayega wah isliye kyunki abb wah subclass abstract class ban chuka hai (RULE HAI) aur u know we
 cannot create object of  this particular subclass as it is  now a abstract class..aur aap toh uss subclass
 ka already object bana k baith gaye the ...for explaination see the below code '''

#points about abstract class :-
'''1.  Abstract classes are classes that contain one or more abstract methods.
2.  An abstract method is a method that is declared, but contains no implementation.
3.  Abstract classes cannot not be instantiated(means u cannot create object/instance for such class),
    and require
    subclasses to provide
    implementations for the abstract methods.
    *abstract class is considered as blueprint for other classes
4.  Subclasses of an abstract class in Python are not required to implement abstract
    methods of the parent class.'''
    #explaination for above 4th point (from line 19-40)
'''In Python, abstraction is a concept in object-oriented programming (OOP) where you can define abstract 
classes that cannot be instantiated and may contain abstract methods, which are methods without any
implementation in the abstract class. Subclasses of an abstract class are required to provide 
implementations for these abstract methods, unless they are also marked as abstract classes.

However, according to the statement you provided, subclasses of an abstract class in Python are
not required to implement abstract methods of the parent class. This means that if an abstract class
defines abstract methods, its subclasses are not obligated to provide implementations for those methods.
    This is in contrast to other programming languages that enforce strict implementation of abstract
    methods in subclasses.

This behavior in Python provides flexibility to the developers, allowing them to choose which
abstract methods to implement in the subclasses based on the specific requirements of their application.
 It can be useful in cases where different subclasses of an abstract class may have different 
 functionalities and may not need to implement all the abstract methods defined in the abstract class.

However, it's important to note that if a subclass of an abstract class does not provide ' \
           'implementations for all the abstract methods of the parent class, then the subclass ' \
           'itself will also be considered as an abstract class, and cannot be instantiated until all' \
           ' the abstract methods are implemented. This means that while it is not required to implement' \
           ' all the abstract methods in the subclasses, doing so is necessary if you want to create ' \
           'an instance of the subclass.'''

#this is the syntax to achieve abstraction in python
'''Syntax :
from abc import ABC, abstractmethod #abc is the module's name and ABC is the abstract class defined 
                                    #in that module
class Employee(ABC):  #class Employee is the abstract class as it is subclass of the class ABC
    #abstract methods
    #concrete methods
Abstract methods:- method that has a declaration but does not have an implementation.
Concrete methods:- Normal methods'''


#example
from abc import ABC,abstractmethod
class Car(ABC):         #here see a point to make Car an abstract class
                        #1. inherit from ABC and 2. give it at least one abstract method
    @abstractmethod
    def mileage(self):
        pass
    def colour(self):
        print("white")
class Maruti_Suzuki(Car):
    def mileage(self):  #if for line no. 62 and 63 , u write jst pass means no implemention of abstract
        print("mileage is 30 kmph") # method mileage the Maruti_Suzuki class is now a abstract class
        #listen ...it is a subclass now ...if u wanna make it abstract class jst do not implement any
        # abstract methods of the parent abstract class Car and then now it is now an abstract class
        #isme Car jaisa nahi hai ki ABC se inherit kro aur at least ek abstract class hona hi padega
        '''All abstract methods present in abstract class must be implemented in child
           classes. Else, child class becomes abstract.'''


class TATA(Car):
    def mileage(self):
        print("mileage is 35 kmph")
class Duster(Car):
    def mileage(self):
        print("mileage is 40 kmph")
#c1=Car() #TypeError: Can't instantiate abstract class Car with abstract method mileage
m1=Maruti_Suzuki()
t1=TATA()
d1=Duster()
m1.mileage()
t1.mileage()
d1.mileage()


#point
'''If there is abstract method in class, that class must be abstract class.
means --- then that abstract class  must be inheritaed from ABC class '''