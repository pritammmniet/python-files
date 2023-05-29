class A:
    #def __init__(self):
        #print("class A constructor")
    def feature1(self):
        print("Feature 1 is working")
    def feature2(self):
        print("Feature 2_A is working")
class B:
    #def __init__(self):

        #print("class B constructor")
        #super().__init__()
    def feature2(self):
        print("Feature 2_B is working")
    def feature4(self):
        print("Feature 4 is working")

class C(B,A):
    def feat(self):
        super().feature2()

    #def __init__(self):

        #print("class C constructor")
        #super().__init__()
    def feature5(self):
        print("Feature 5 is working")

#a1=A()
#a1.feature1()
#a1.feature1()
c1=C()
c1.feat()
#b1.feature1()
#b1.feature2()
#b1.feature3()
#b1.feature4()
