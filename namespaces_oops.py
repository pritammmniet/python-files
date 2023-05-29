#scope of a variable def:-
#scope of a variable is a part of the program in which that variable is recognized
'''A namespace is a system that has a unique name for each and every object in Python. An object might be
a variable or a method. Python itself maintains a namespace in the form of a Python dictionary. Let’s go
through an example, a directory-file system structure in computers. Needless to say, that one can have
multiple directories having a file with the same name inside every directory. But one can get directed
 to the file, one wishes, just by specifying the absolute path to the file.
On similar lines, the Python interpreter understands what exact method or variable one is trying to
point to in the code, depending upon the namespace. So, the division of the word itself gives a little
more information. Its Name (which means name, a unique identifier) + Space(which talks something related
to scope). Here, a name might be of any Python method or variable and space depends upon the location
from where is trying to access a variable or a method.
'''


#read this article link---   https://realpython.com/python-namespaces-scope/
'''iss link pe tutorial padhte waqt bahut saare doubt aa skte hai to niche wah saare points jo maine likhe 
hai meri samjh k according jo may be ki aage future mein modification chayiye unhe idk ...look!'''
#enclosing hindi meaning----संलग्न
#1.outer function is called by the main program ////(a satement aise hi)
#2.outer function -enclosing function //////inner function ---enclosed function
#3.globals is  in-built function name  and u know global() is storing the value returned by the function name
 #gobals
#4. look here __builtins__ is nothing but the name to a built-in module whose name is builtins and if u
# print the dir(__builtins__) then u will  get  a list of built-in methods and variable .
#5.def f():
     s="foo"
     loc=locals()
     '''here locals() is not the actual local namespace but a copy of current(current isliye bola kyunki 
      abb actual local namespace bhi badalta rehta hai ) actual local namespace and var
     name loc is jst pointing to this copy and nothing more ...yup it is different from globals() beacause wah 
     actual global namespace hota hai na ki koi copy.. samjhe?'''
     print(loc)
     x=89
     print(loc)
     loc["s"]="bar"
     print(loc,s) #see here s is not changed because s badla toh hai but in the copy of actual local
              # namespace
     new_loc=locals() #explain dekho current ka local namespace ka mtlb
     print(new_loc)
f()

#6.