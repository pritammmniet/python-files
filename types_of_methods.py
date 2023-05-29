class Car:
    var1=7
    def __init__(self):
        self.name="ram"
    def inst_method(self):#instance method but see  it can alter the state of both class variable as
                        #well as of instance variable
        Car.var1=10
    @classmethod
    def class_method(cls):
        print(9)
        print(Car.var1)
        Car.var1=100
        print(Car.var1)
        print("instance variable",c1.name) #dekho yeh bhi ek instance var but koi dikkat nahi hai Qki yahan
                                            #self nahi chayiye
        #print(self.name)#means they work only with class variables ...got it ??
        #self.name="sita"#it cannot  alter/change the state of instance variable
        #aur kitna logical yeh kyunki self.name mein aapko self chayiye wah aap self kahan se laoge
    @staticmethod
    def static_method():
        print("this is a static method")


c1=Car()
c1.inst_method()

c1=Car()
Car.class_method()
Car.class_method()#way to call it when u r using dec..@classmethod
#Car.class_method(Car)#way to call the same class method when u are not using dec ...@classmethod
Car.static_method()



