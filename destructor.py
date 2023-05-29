class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        print("FileHandler object created for:", self.filename)

    def open_file(self):
        print("Opening file:", self.filename)

    def close_file(self):
        print("Closing file:", self.filename)

    def __del__(self):
        print("FileHandler object deleted for:", self.filename)
        self.close_file()

# Creating an object of the FileHandler class
file1 = FileHandler("file1.txt")

# Calling methods on the object
file1.open_file()
file1.close_file()

# Deleting the object
del file1   #listen the way __init__ is called by the python intrepretor .at the time of object creation ..in
            #the same way __del__ is called when python intrepretor deletes the object or somehow it has gone
            #out of the scope
'''In the example above, the FileHandler class has a destructor __del__ that is automatically called when
 the object file1 is deleted using the del statement. The destructor prints a message indicating that 
 the object is being deleted and calls the close_file() method to close the file associated with the 
 object.

Here are some key points to understand about destructors in Python:

Automatic Execution: Destructors are automatically called by the Python interpreter when an object
 is deleted or goes out of scope. You do not need to explicitly call the destructor.

Cleanup Operations: Destructors are typically used to perform cleanup operations, such as
 releasing resources (like file handles or network connections) or performing other cleanup tasks
  (like closing database connections or releasing memory) before the object is destroyed.

self Parameter: Like constructors, destructors also have a self parameter that refers to the instance of 
the object being deleted. This allows you to access and modify the attributes and methods of the object
 within the destructor.

Object Deletion: Objects can be deleted explicitly using the del statement or when they go out of scope
 (e.g., when the program finishes execution). When an object is deleted, its destructor, if defined, is
  automatically called before the object is destroyed.

Multiple Destructors: Python does not support multiple destructors with different names or parameter 
lists. If a class defines more than one destructor, only the last one defined will be called when the object is deleted.

Inheritance and Destructors: If a class inherits from a superclass and defines its own destructor, 
the destructor of the superclass is not automatically called. If you need to perform cleanup operations 
in the destructor of the superclass, you should explicitly call the superclass's destructor using the super() function.

Here's an example illustrating the use of a destructor in the context of class inheritance'''
class Parent:
    def __init__(self):
        print("Parent object created")

    def __del__(self):
        print("Parent object deleted")

class Child(Parent):
    def __init__(self):
        print("Child object created")

    def __del__(self):
        print("Child object deleted")

# Creating an object of the Child class
child1 = Child()

# Deleting the object
del child1
#output
Child object created #u can see preference over super class

Child object deleted ##u can see preference over super class



