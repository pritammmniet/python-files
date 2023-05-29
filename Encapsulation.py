'''Encapsulation is a concept in object-oriented programming (OOP) that involves hiding the internal
 state and implementation details of an object from the outside world, and exposing only the essential
  interfaces or methods that can be used to interact with the object. It is one of the four pillars of OOP,
   along with inheritance, polymorphism, and abstraction.

In Python, encapsulation can be achieved using conventions and access modifiers, which determine the
visibility and accessibility of class members (i.e., variables and methods). There are three types of
access modifiers in Python:

Public: Members declared as public are accessible from anywhere, both within and outside the class.

Private: Members declared as private are accessible only within the class itself. They are denoted by
double underscores (__).

Protected: Members declared as protected are accessible within the class and its subclasses.
They are denoted by a single underscore (_).

Now, let's look at an example to understand encapsulation in Python in depth:'''


'''class BankAccount:
    def __init__(self, account_number, balance, owner_name):
        self.__account_number = account_number
        self.__balance = balance
        self.__owner_name = owner_name

    def deposit(self, amount):
        self.__balance += amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

    def get_account_info(self):
        print("Account Number:", self.__account_number)
        print("Owner Name:", self.__owner_name)
        print("Balance:", self.__balance)'''

'''In this example, we have a BankAccount class that represents a bank account with encapsulated
 data members such as account_number, balance, and owner_name. These data members are declared as private by prefixing them with double underscores.

The class also has methods such as deposit(), withdraw(), get_balance(), and get_account_info(), which 
provide the essential interfaces to interact with the object. These methods are declared as public and
 can be accessed from anywhere.

The deposit() method allows depositing an amount into the account and updates the balance. 
The withdraw() method allows withdrawing an amount from the account if the balance is
 sufficient, otherwise, it prints an error message.

The get_balance() method returns the current balance of the account, and the get_account_info() method 
prints the account number, owner name, and balance of the account.

Here's an example of how we can use the BankAccount class:'''
'''# Creating a BankAccount object
account = BankAccount("1234567890", 1000, "John")

# Accessing public methods to deposit and withdraw
account.deposit(500)
account.withdraw(200)

# Accessing public methods to get balance and account info
print("Current Balance:", account.get_balance())
account.get_account_info()

# Attempting to access private data members (results in an AttributeError)
#print(account.__account_number)'''
'''In this example, we create a BankAccount object and use the public methods deposit(), withdraw(), 
get_balance(), and get_account_info() to interact with the object. However, when we try to access the
 private data member __account_number directly, it results in an AttributeError, indicating that the
  private data member is not accessible from outside the class.

This demonstrates how encapsulation allows us to hide the internal state and implementation details 
of an object, and provides controlled access to essential interfaces'''





#code for protected access modifier
'''Certainly! Protected access modifier in Python is denoted by a single underscore prefix before the name 
of a variable or a method. It indicates that the member is intended to be accessed within the class and its
 subclasses, but not from outside the class. However, unlike private members, protected members can
  technically still be accessed from outside the class. Let's take a closer look with an example:
python
'''


class BankAccount:
    def __init__(self, account_number, balance, owner_name):
        self._account_number = account_number  # protected member
        self._balance = balance  # protected member
        self._owner_name = owner_name  # protected member

    def deposit(self, amount):
        self._balance += amount
        print("Amount deposited:", amount)

    def get_account_info(self):
        print("Account Number:", self._account_number)
        print("Owner Name:", self._owner_name)
        print("Balance:", self._balance)


class SavingsAccount(BankAccount):
    def __init__(self,account_number, balance, owner_name, interest_rate):
        BankAccount.__init__(self,account_number, balance, owner_name)
        #replacement of line no 114 is   super()__init__(self,account_number, balance, owner_name)
        self._interest_rate = interest_rate

    def calculate_interest(self):
        interest = self._balance * (self._interest_rate / 100)
        print("Interest calculated:", interest)
        print(sav_account._balance) #done to show here init of parent class works for obj of child class ofc
sav_account=SavingsAccount(7028348,1500,"ram",5)
sav_account.calculate_interest()


#see how a private class variable is accessed from outside of the class
class MyClass:
    __hiddenVar=12
    def add(self,increment):
        self.__hiddenVar+=increment
        print(self.__hiddenVar)

MyObject=MyClass()
MyObject.add(3)
MyObject.add(8)
print(MyObject._MyClass__hiddenVar)
#explain for this (last line ) is below
'''Certainly! The last line of the code print(MyObject._MyClass__hiddenVar) is attempting to access the
 value of the private attribute __hiddenVar of the MyClass class using name mangling.

In Python, when a class attribute is prefixed with double underscores (__), it is considered as a private 
attribute and Python uses name mangling to make it difficult to access from outside the class. 
Name mangling involves adding a prefix of _classname before the attribute name, where classname is
 the name of the class.

In this case, the private attribute __hiddenVar of the MyClass class is being accessed using name 
mangling with the syntax _MyClass__hiddenVar, where _MyClass is the name of the class. This is a way
 to access the private attribute from outside the class, although it is not recommended as it goes against
  the intended encapsulation and abstraction of class attributes.

The print() statement in the last line of the code will print the value of the private
 attribute __hiddenVar of the MyClass class, as updated by the add() method calls on the MyObject
  instance. However, it's important to note that directly accessing private attributes from outside the 
  class using name mangling is not a recommended practice in Python, and it's better to use public methods
   or properties to interact with class attributes.'''

# my note ---dekho in case of protected variable ...kuch programmers ne bro code banaya ki agr _ lagakar
#variable/methods hai toh outside se access mt kro ...krne ko kr skte ho but mat kro n ...krna hai toh method
# bano aur kro ...aisa isliye hota hai possible kyun ki python ne abhi tk nahi mana hai ki aisa bhi kuch
#hota hai ....
#same acc to chat gpt
'''It's worth noting that in Python, the convention of using a single leading underscore to indicate
 protected variables is not enforced by the language itself, but rather a common convention followed by 
 many Python programmers. It's ultimately up to the developers to follow these conventions and respect the
  intended privacy of variables in their code.'''


#but in case of private variable aisa nahi hain kyunki yahan pr python thoda samjhta hai ..wah protection k
# liye variable ko mangle/convert kr deta kuch iss syntax mein {_MyClass__hiddenVar} toh abb yeh chupa hua
# naam hai ussi same variable ka toh if u want to access toh iss naye naam se access krna try kro ...
#kaam jo jayega
