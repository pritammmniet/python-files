#see the working of super in the case of class method through an example
class Base:
    @classmethod
    def f(cls, x):
        print("Base.f", cls, x)
class Derived (Base):

    @classmethod
    def f(cls, x):
        print("Derived.f", cls, x)
        super().f(x)
        print("Derived.f finished")
def fun():
    d=Derived()
    Derived.f(42)
fun()

#yeh niche wala ek accha example toh dekh lena dict k context mein hai 
class LoggingDict(dict):
    def __setitem__(self, key, value):
        print (f'Setting {key}: {value}')
        super().__setitem__(key, value)
    def __getitem__(self, item):
        print (f'Getting {item}')
        return super().__getitem__(item)
    def __delitem__(self, key):
        print (f'Deleting {key}')
        super().__delitem__(key)
def logging_dict_example():
    print("LOGGING DICT EXAMPLE")
    d = LoggingDict()
    d["key1"] = "subscribe"
    x = d["key1"]
    del d["key1"]
    print()
logging_dict_example()