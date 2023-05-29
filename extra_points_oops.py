#point no 1
'''class Computer:
    def __init__(self):
        self.__maxprice=900
    def sellprice(self):
        print(f"selling price of computer is {self.__maxprice}")
    def set_maxprice(self,value):
        self.__maxprice=value
c1=Computer()
c1.sellprice()
c1.__maxprice=1000#here what actually happens is that see using init method we jst appoint something to
                #inst. variable attached to obj ..here the same has been done but directly without the help
                #of any init method
c1.ram=89
print(c1.ram)
print(c1.__maxprice)'''


#point no 2
'''class MyClass:
    hiddenVar=12
    def add(self,increment):
        self.hiddenVar+=increment
        print(self.hiddenVar)

MyObject=MyClass()
MyObject.add(3)
MyObject.add(8)
print(MyObject.__class__.hiddenVar)# here using __class__ we are able to use class variable using object name
#normally we do as Myobject.hiddenVar but here with the same name there is instance variable .that's why'''

#point no 3
'''class Car:
    wheels=4
    def set_method(self):
        Car.wheels=8
        #self.wheels=8 #through this way u cannot update the value of wheels...
    def __del__(self):
        self.wheels=8

c1=Car()
c1.set_method()
print(Car.wheels)'''

#point no 4
'''class Car:
    wheels=4
    def __init__(self): #here kitna bhi constructor bana lo excute toh bs phla hi hoga
        print("constructor no 1")
    def __int__(self):
        print("constructor no 2")


    def __del__(self):
        print("destructor no 1")
    def __del__(self):
        print("destructor no 2")#here kitna bhi destructor bna lo ...excute toh kewal last wala hi hoga

c1=Car()
del c1'''

#point no. 5
'''#program to check both if are keywords then why one of them is not recognized by python intrepretor
import keyword
print(keyword.iskeyword("True"))
print(True)


print(keyword.iskeyword("global"))
#print(global) #here the reason behind is that global  is a keyword but it is not in built-in namespace
            #In short, while "global" is not listed in the dir(__builtins__) output, it is still an
# important part of the Python language and is recognized by the Python interpreter.'''


#point no . 6
'''#here we are to understand ki kaise object/instance of a class, class level data attribute(in short class
# variable) ko access kar pata hai with the help of an example
class Program:
    language="python"

p1=Program()
print(Program.language)#yahan tk ok lag raha hai qki class ne class variable ko access kar liya .kya ho gya

print(p1.language)#benchod yeh kya hai ...ek instance ne kaise kar liya ek class variable ko access

print(Program.__dict__)
print(p1.__dict__)#actually hota kya hai n abb p1 k namespace yani iske dict mein koi"language" naam ka key 
                #hai hi nahi toh phle yeh p1 ke namespace mein serach karta hai aur agr iss namespace mein
                #nahi milta toh phir yeh class k namespace mein uss key k liye value search karta hai aur 
                #agr wahan mil gaya toh theek hai nahi toh ant mein jakar attribute error de dega
#aur kuch jaan lo kaise uss class attribute ko access kar sakte ho
print(Program.language)
print(Program.__dict__["language"])
print(p1.language)
print(getattr(Program,"language"))
print(getattr(p1,"language"))'''

#point no. 7
'''class Program:
    def my_method(self):
        pass
p1=Program()
print(Program.my_method)
print(p1.my_method)#output of this <bound method Program.my_method of
                # <__main__.Program object at 0x0000016D355A2710>> and this inside<> is the object p1 itself
print(p1.my_method.__func__)#method attribute __func__
print(p1.my_method.__self__) #method attribute __self__'''
#point no. 8
'''class Person:
    def say_hello(self):
        print("Hello World!")
p1=Person()
print(Person.say_hello is p1.say_hello.__func__)
p1.say_hello.__func__(p1.say_hello.__self__)#calling instance method
Person.say_hello(p1)#caling instance method through another way
print(Person.say_hello is p1.say_hello)#o/p is False and why not ...it is because Person.say_hello is a reg
#function but p1.say_hello is not anymore a req function but a method bound to the object p1
#and ofc Person.say_hello(p1) is p1.say_hello() as they are not function or method but a value and value is 
#same in both the cases so that is the reason the o/p will be True


yahan dhyan do to u can notice that p1.say_hello is jst the method name 
and Person.say_hello is not the method name but the name of function 
'''
#point no. 9
'''class Person:
    legs=2
    def set_name(instance_obj,name):
        instance_obj.name=name

p1=Person()
p1.set_name("rahul")
#abb dekho doubt yeh hai ki legs ek attribute hai ...specifically bole toh class attribute ...right ??
#but accessible hai don se
print(Person.legs)
print(p1.legs)
#but yeh jo instance attribute hai name yeh kyun nahi dono se accessible ho jata in the same fashion
print(p1.name)
#print(Person.name)
#abb chup chap reason sunn lo
print(Person.__dict__)
print(p1.__dict__)
#reason yeh hai ki agr legs p1 ko instance dict mein nahi mila toh wah muh utha ke class dict mein chala
#gya ...samjhe ?? toh usse legs ki value mil gayi which is 2 but in case of name attribute yeh hua ki
#p1 ko toh mil gayi kyunki yeh name tha p1 ke dict. mein lekin class k dict mein yeh nahi tha aur class ne
#yeh attribute ne phle apne dict mein search kara aur nahi mila toh instance dict mein nahi aaya hai bol
#diya ki error aa gya hai wahi pe turant
print("name" in Person.__dict__)#returns False'''

#point no 10
'''class Person:
    def set_name(instance_obj,name):
        instance_obj.name=name
p1=Person()
#doubt yeh hai ki agr set_name ek instance method hai toh wah q nahi p1.__dict__ mein rehta hai ...balki
#wah Person.__dict__ mein rehta hai
#ans.
#The reason for this behavior is that Python is designed to optimize the use of memory, and storing the
#method in the class's dictionary is more memory-efficient than storing a separate copy of the method in
#' each instance's dictionary.'''

#point no 11
'''class Person:
    pass
p1=Person()
p1.other_func=lambda *args: f"other_func has been called from {args} "
print(p1.other_func())#o/p other_func has been called from ()
print(p1.other_func)
print(Person.other_fun()) #u cannot do this as this is the attribute of instance p1 only and accessible only
#by it
print(p1.__dict__)
#yeh kya ho gya p1.other_func ek method kyun nahi hai aur p1 as the first argument kyun nahi pass hua
#mtlb yeh aise kyun behave kar raha hai jaise yeh class level pe defined kara gaya ho aur aise use kara ja
#raah hai Person.other_func ...
#ans.. dekho baat yeh hai n bhaisahab ki yeh jo other_func hai n because of the line p1.other_func
#wah ussi instance p1 k namespace mein ghus gya hai aur jb python yeh dekh leta hai ki object ko apne hi
#namespace mein wah function mil gaya toh wah usse function bol deta hai aur p1.other_func mein p1 ko
#as the first argument pass nahi karta hai ...--pritam yeh reason nahi hai bs padh lo aur ignore kar do



dekho yeh ek aur official reason ....yahi ki agr function class k andr define ho gya aur aage use hoga 
by the instance of the class tb same function will be treated as method bound to that instace but agr koi
function outside class define hoga yani during runtime tb wah ek function ke tarah hi treat hoga 
samhje ??'''

#point no 12
'''class Person:
    def __init__(self):
        print(f'Initializing a new Person object: {self}')
p1=Person()#Initializing a new Person object: <__main__.Person object at 0x000001AC5D522810>

print(p1)#<__main__.Person object at 0x000001AC5D522810>
Person()#Initializing a new Person object: <__main__.Person object at 0x000001AC5D522850>
#note aap kripya id k digits pe dhyan mt do q ki har run k baad badalta rehta hai..feelings samjho
#abb doubt yeh hai ki last statement Person() ka ek output hai sir ...lekin prob kya hai abb call hua toh
#print statement toh excute hoga hi n __init__ method ka ...arre baat yeh hai ki iske output mein jo
#instance hai wah kahan se aa gaya hai ...wah toh p1 bhi nahi hai ...
#ans.
The last statement Person() creates a new Person object but since it is not assigned to any variable, it 
is immediately destroyed after its initialization. The __init__ method of the new object is called and it 
prints a message to the console, but there is no reference to the object left so it becomes eligible for
 garbage collection.

Therefore, the last statement will print the message "Initializing a new Person object: <main.Person 
object at <memory address>>" to the console, where <memory address> is the memory location where the new 
object was temporarily created. However, since the object is immediately destroyed, there will be no 
reference to it and it will not be possible to access or manipulate it in any way.
'''

#point no 12
'''class Program:
    language="python"
p1=Program()
#hum abb jakar hum chahte hai ek method which is bound to our instance p1 but if we do like this
#p1.say_hello=lambda : "Hello World!"
#toh yahan pe say_hello koi method nahi hai balki yeh ek nrml function hai
#print(p1.say_hello) #o/p <function <lambda> at 0x00000186A7230540> clearly mention it is a function
#now let's make it a method ...
from types import MethodType
p1.inst_method=MethodType(lambda self : f"inst_method has been called bound to {self}",p1)
print(p1.inst_method)#o/p <bound method <lambda> of <__main__.Program object at 0x00000237CE2326D0>>
#clearly it is mentioned that inst_method is a method bound to the instance p1
print(p1.__dict__)



#ek aur tarika by me pritam which may be right/wrong 
class Program:
    language="python"
p1=Program()
Program.reg_func=lambda self : f"reg_func has been called from the instance {self}"
print(p1.reg_func())
print(p1.__dict__)
print("reg_func" in Program.__dict__)'''

#point no 13
'''let's talk about property ..ki kaam kaise karta hai :-
abb iski need hi kyun padi ...wah bhi janna important hai ...abb maano koi protected instance attribute _age
hai toh acc to the interface of the code we should  not use access the _age attribute directly and if we do 
{we know we can in python but not in java } toh yeh breaking of interface of the code kehlata hai toh 
python has solution hai for this ...which is the use of concept of property


In Python, an attribute is called a property of the class when it is defined using the property() function
 or the @property decorator.
 
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError('Age must be an integer')
        if value < 0 or value > 120:
            raise ValueError('Age must be between 0 and 120')
        self._age = value
p=Person(79)
print(p.age) 


yahan dekho 
1)_age is a protected instance attribute 

2)age is that property of the class and u can also say it a class attribute
expln for 2)
 In Python, a property object can be referred to as a "property" or an "instance property" because
  it behaves like an instance attribute even though it is actually an object of the property class.
  here property is a in-built class


toh aap yahan dekho ki print(p.age) karne par value 79 aa gayi ...aur humne _age attribute ko directly 
access bhi nahi kiya phir
bhi humne uski hi value ko retrieve kar liya hai ...toh interface of the code bhi break
nahi hua ...accha hai na plan ..hmm ...aur bhi fyade hai property age use karne k ..jaise u can validate
the value which is the set value for the instance attribute _age

aise hi note it ;--
 Getter: A method that allows you to access an attribute in a given class
Setter: A method that allows you to set or mutate the value of an attribute in a class

abbhi upr k example mein property age dekha that was created in one manner and aage u will see how 
property is created in a different way using property()
class Person:
    def __init__(self, name):
        #self.name=name #abhi jb value ko itna gyan de rahe ho ki tughe aisa hona hai toh wah gya name ko 
        #bhi do that's why isse aise use kiya gya toh agr class instantiation k time hi name invalid ho gya
        #toh yeh error yahi aa jayega
        self.set_name(name)
        
    def get_name(self):

        return self._name
    
    def set_name(self, value):
        if isinstance(value, str) and len(value.strip()) > 0:
            # this is valid
            self._name = value.strip()
        else:
            raise ValueError('name must be a non-empty string')
    def del_name(self):
        print("del_name has been called")
        del self._name
        # (fget=None, fset=None, fdel=None, doc=None) constructor of class property --source gpt
    name = property(fget=get_name,fset=set_name,fdel=del_name,doc="what a nazara!")
    # upar name alawa ram bhi use ho skta hai..but yeh cool lagta hai when u say self.name rather self.ram
p=Person("alex")
#dekho in python u can use bare attributes ...bs yeh getter aur setter ki need tb hoti hai when u think 
#ki now u need validation before setting the value to the instance attribute  aur chlo samjh itna smjh gya 
#toh abb benchod yeh property kya hai ..dekho yeh abb aise likho 
print(p.get_name())
print(p.set_name("ram"))
print(p.get_name())

#toh abhi using these setter and getter we are not breaking the interface of the code so will not face issue
#lekin it is little bit complex ...so to make it easy ...now we will use the concept of property
print(p.name)#here using p.name ..get_name method has been called bound to the object p
            # u can also use this way print(getattr(p,"name")
p.name="riya"#here using this line ...set_method has been called bound to the object p
         #u can also use this way setattr(p,"name","riya")
print(p.name)
print(p.name is p.get_name())


#abb choti si kahani /or something like exception
print(p.name)
print(p.__dict__)
p.__dict__["name"]="chiya"
print(p.__dict__)
print(p.name)#here yahan "name" attribute is not that instance attribute "name" stored in the dictionary
#of the object p but this is property name which is a class -level attribute ...u can find
# in Person.__dict__ ...lekin aisa hua kyun yeh toh phle instance p ke dict mein search karega na for any
#attribute agr nhi milta tb na jata ....
#ans yeh bata diya hai ...abhi charcha baki hai waise ...dekho "name" ="sita" kara gya bypassing the setter
#method which is the breaking of the interface aur toh whenever there will be like p.name ....it will look
#for the property "name" not for the instance attribute "name" in p.__dict__ as it was not set using setter
#method



#abb bahut ho gayi charcha , aao abb charcha karte hai fedel pe
print(p.__dict__)
del p.name
print(p.__dict__)
#abb doc pe charcha 
The doc attribute is an optional argument for the property() function that allows you to specify a
docstring for the computed attribute that is created. In the code you provided, the name property is 
created with property(fget=get_method, fset=set_method, doc="what a nazara!").

The doc string "what a nazara!" is a short description of the name property that will be displayed 
when you access the property's docstring using the help() function or by printing the __doc__ attribute' 
                            ' of the property object. For example, if you run help(p.name) or' 
                            ' print(p.name.__doc__), you should see "what a nazara!" displayed as ' 
                            'the docstring for the name property.

Docstrings are used to provide useful information about the code and its usage, and they are an
important aspect of writing clear and maintainable Python code.'''





#point no 14
'''hum yahan padh rahe class aur static methods k baare mein'''
#hum kis tarah se function ko access karte wah decide karta hai uski behaviour ko

'''class MyClass:
    def hello():
        print("hello")
m=MyClass()
print(MyClass.hello)#o/p <function MyClass.hello at 0x000001E2702BC900>
print(m.hello)#o/p <bound method MyClass.hello of <__main__.MyClass object at 0x000001E2702C2890>>
MyClass.hello()'''
#m.hello()#o/p TypeError: MyClass.hello() takes 0 positional arguments but 1 was given
#here u can see hello ko class se access kro toh it is a function and if access that with instance then
#it is a method bound to the instance m
#infact any function defined inside class will be handled as method bound to instnace be default if called
#from an instance

#lekin class methods ko farq nahi padta  app instance se access karo ya phir class name se in both cases
#class se bound rehta hai
#let's have an example
class MyClass:
    def hello():
        print("hello")
    def inst_method(self):
        print("instance method")
    @classmethod
    def class_method(cls):
        print("class method")
    @staticmethod
    def staic_method():
        print("static method")
m=MyClass()
print(MyClass.hello)#o/p <function MyClass.hello at 0x0000024C1CD1C900>
print(m.hello)#o/p <bound method MyClass.hello of <__main__.MyClass object at 0x0000024C1CD230D0>>
MyClass.hello()#o/p hello
#m.hello()#o/p TypeError: MyClass.hello() takes 0 positional arguments but 1 was given

print(MyClass.inst_method)#<function MyClass.inst_method at 0x0000023CFED8C720>
print(m.inst_method)#<bound method MyClass.inst_method of <__main__.MyClass object at 0x0000023CFED930D0>>
#MyClass.inst_method()#TypeError: MyClass.inst_method() missing 1 required positional argument: 'self'
m.inst_method()#instance method

print(MyClass.class_method)#<bound method MyClass.class_method of <class '__main__.MyClass'>>
print(m.class_method)#<bound method MyClass.class_method of <class '__main__.MyClass'>>
MyClass.class_method()#class method
m.class_method()#class method

print(MyClass.staic_method)#<function MyClass.staic_method at 0x000002214B5ADDA0>
print(m.staic_method)#<function MyClass.staic_method at 0x000002214B5ADDA0>
MyClass.staic_method()#static method
m.staic_method()#static method
#mere mann mein ek doubt aata hai ki agr reg function can be used inside a class then what is the point of
#using static methods dekho fark hai ...for a reg func ..if u call it from the class then it is ok
#but once u call it from the instance then it will behave like a method bound to that instance but in case
#static method ...does not matter ...it will be always a function either u call it from a instance or class

#one fact about static method ...
#it is highly discourage from a section of devs because the function which is static method can also be
#defined at the module level aur uska ek fayda yeh hoga ki wah class name ya insatnce jaisa prefix nahi
#lagana padega usse u can diectly use it








