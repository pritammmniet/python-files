#kisi bhi class k liye mro pata kiya ja skta hai abb ya toh manually kar lo jime glti hone k high chances
#hai toh iske liye do tarika hai python mein to find mro with the help of python itntrepretor
#1. class_name.mro()   where mro() is in-built method and it returns list
#2. class_name.__mro__ where __mro__ is a in-built class variable  where it returns a tuple

#see
def the_properties_of_mro_you_should_care_about():
    class A: #(A,object)
        pass
    class B: #(B,object)
        pass
    class C(A,B): #(C,A,B,object)
                    #(A,   object) ---parent class A should have mro that will be sub-seq of child class C
                    #   (B,object)----parent class B should have mro that will be sub-seq of child class C
        pass
    class D(A,C):   #error reason  correct would be class D(C,A)
                    #reason : isme dekho toh A C se phle aaega but in class C(A,B) mein C phle aayega A se
                    #that led to a cintradiction toh aisa case mein python aise class banne nahi dega and if
                    #if u will try then u will get an error
        pass
the_properties_of_mro_you_should_care_about()