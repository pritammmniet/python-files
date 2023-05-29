'''there are two types of varoables in class
1. class/static variable
2. instance variable'''
'''dono mein bs basic difference yeh hai ki agar class variable mein koi change hua toh wah change har obj
mein dikhega but wahi instance variable mein yeh hota hai ki  agar koi change kiya kisi individual instance 
variable mein toh wah change kewal usi mein dikhega'''
class Car:
    wheels=4
    def __init__(self):
        self.mil=10
        self.com="BMW"

c1=Car()
c2=Car()
c1.mil=8#yeh wala change kewal isi object ko effect karega
Car.wheels=5#here class var. change hua hai toh dono obj var mein yeh effect dikhega
print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,c2.wheels)
