'''let's understand with the help of an example'''
class College:
    def __init__(self):
        print("outer class constructor")
    class Student:
        def __init__(self):
            print("inner class constructor")
        def displayS(self):
            print("inner class methhod")
    def displayC(self):
        print("outer class method")
c=College()
c.displayC()
s=c.Student() #u can also use s=College().Student() or s=College.Student() bs logic yeh hai ki first word
                #bata de ki Student class kis class k andr hai ..toh 3 upr tareeko se ho skta hai
s.displayS()