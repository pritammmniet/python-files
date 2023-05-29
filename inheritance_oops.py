#types of inheritance
#there are 5 types of inheritance
#1.single level inheritance
#2. multi-level inheritance
#3. multiple inheritance
#4. hierarchical inheritance
#5. hybrid inheitance

'''1.Single inheritance: In this type of inheritance, a class inherits properties and behavior from a
single parent class. The syntax for single inheritance is as follows:
class ParentClass:
    # parent class definition

class ChildClass(ParentClass):
    # child class definition'''

'''2. Multiple inheritance: In this type of inheritance, a class inherits properties and behavior from
 multiple parent classes. The syntax for multiple inheritance is as follows:
 class ParentClass1:
    # parent class definition

class ParentClass2:
    # parent class definition

class ChildClass(ParentClass1, ParentClass2):
    # child class definition
'''

'''3. Multi-level inheritance: In this type of inheritance, a class inherits properties and behavior 
from a parent class, which in turn, inherits from another parent class. The syntax for multi-level
 inheritance is as follows:
 class GrandparentClass:
    # grandparent class definition

class ParentClass(GrandparentClass):
    # parent class definition

class ChildClass(ParentClass):
    # child class definition
'''

'''4. Hierarchical inheritance: In this type of inheritance, multiple child classes inherit properties 
and behavior from a single parent class. The syntax for hierarchical inheritance is as follows:
class ParentClass:
    # parent class definition

class ChildClass1(ParentClass):
    # child class 1 definition

class ChildClass2(ParentClass):
    # child class 2 definition
'''

#parent class --- super class
#child class---sub class , derived class
#simple example to show the inheritance

'''class A:
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")
class B(A):
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")
a1=A()
a1.feature1()
a1.feature2()


b1=B()
b1.feature1()#here u can clearly see that both the methods of class A has been inherited from A to B..
            #so easy
b1.feature2()
b1.feature3()
b1.feature4()'''


#now anothere example
'''class Employee:
    raise_amt=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.email=first+"."+last+"@gmail.com"
        self.pay=pay
    def fullname(self):
        return "{} {}".format(self.first,self.last)

    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10
dev1=Developer("Corey","Schafer",50000)
print("pay before raise",dev1.pay)
dev1.apply_raise()
print("pay after raise",dev1.pay)'''

'''expn--- for the above code 
#output
pay before raise 50000
pay after raise 55000
here u can see clearly the raise_amt i.e 1.10 is of class Developer has been used in the method apply_raise
not the raise_amt i.e 1.04 of class Employee..logical hai ...abb tumhe batao self.raise_amt mtlb here 
dev1.raise_amt ka value kya hi ho skta hai
'''
'''# let's dive into super() function
bhaiya mughe abhi ghnta samjh nahi aaya ..time nahi tha ..but u can do using the link 
https://realpython.com/python-super/
now suno super() mein do parameter hota hai first parameter hota hai subclass aur second parameter hota hai
ussi subclass ka object (self) abb dekho yeh daalte nahi hai kyunki python bhi default yahi samjhta hai
samjhe?? aur dekho abb subclass daalne se yahi hota hai ki super iss subclass se upar yani iske parent class
mein wah prescribed .method ya .attribute search krta hai 
basically super(subclass name , object of this subclass)

#code for the above 
class A:
    class_var=10
    def a_method(self):
        print("class A method")

class B(A):
    class_var = 67
    def b_method(self):

        print("class B method")
        super(B,self).a_method()#here using super()... accessing method of class A
        print(super().class_var)#here using super(),,,accessing class variable of class A 

b1=B()
b1.b_method()

'''


class Employee:
    raise_amt=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.email=first+"."+last+"@gmail.com"
        self.pay=pay
    def fullname(self):
        return "{} {}".format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        '''mera expln for the function super() is discussed just above this example'''
       # Employee.__init__(self,first,last,pay)#another way to use the __init__ method of parent class
        self.prog_lang=prog_lang

dev1 = Developer("Corey", "Schafer", 50000,"python")
print(dev1.email)
print(dev1.prog_lang)

#let's see about these two function
print(isinstance(dev1,Developer))
print(issubclass(Developer,Employee))

#note--
'''In summary, class Person(object) in Python means that the Person class is defined as a subclass of
 the object class, and therefore inherits all of the methods and attributes of the object class. However,
  since Python 3.x, it's not necessary to include (object) as it is automatically inherited.'''


#here let's study about MRO (method resolution order)
#note;-- HYBRID INHERITANCE ---this type of inheritance has multiple type of inheritance aur iska fig
# ka link hai niche dekh lena

#MRO POINTS;---
'''1. priority is given to child class always


2.MRO search --depth first left to right approach(u can look a pict. pasting into file manager
#C:\Users\pritam mall\Pictures\Screenshots\Screenshot (14).png
#video link --https://youtu.be/oBPwPPuf6Nw
jb aap fig dekhenge toh pata lagega ki mro(p) is PXYABCO
wah pahle p mein dekhega as it is a child class 
then class X and then class Y mein agr nahi toh 
phir wapas aayega X ke parent class mein dekega from left to right which will be then A -B-C 
agr nahi mila abhi tak toh Y ke parent class mein dekhega which are B and C (fig.) but already B and C 
mein dekha ja chuka hai toh yeh dubara search nahi karega ...kyunki yeh chutiya nahi hai ...abb agr 
abhi bhi nahi mila toh ofc last mein bacha class O mein search karega ..samjhe ? 


3. hum mro() function ka use karke ...input class ke object ka attribute ya method kis order mein search 
hoga iss input class ke parent classes mein.....
let's see with the help of an example 
class A:
    pass
class B:
    pass
class C:
    pass
class X(A,B,C):
    pass
class Y(B,C):
    pass
class P(X,Y):
    pass
print(P.mro())
but the output is [<class '__main__.P'>, <class '__main__.X'>, <class '__main__.A'>,
 <class '__main__.Y'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]
 which means order should be PXAYBCO here u can see it is different from the order found manually 
 PXYABCO....now let's do a charcha here  after this tea break
 dekho charcha krna aasan nahi hai ...inheritance mein do hi cheez dimag ka abhi bhosda kar rahi hai aur wah 
 hai super() and mro....lekin krna toh hai aaj nahi toh kal ...smjhe?/
 dekho charcha dekhi hai toh uski alag - alag .py files ...ja ke dekh lo 

'''
