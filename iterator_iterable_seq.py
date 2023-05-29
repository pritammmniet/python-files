#abhi likhna hai
#an example
'''list1=[1,2,3,4,5,6]
my_iterator=iter(list1)#this built-in func. returns the iterator that iterates
# over all the the elements of the iterable one-by-one
#def of iterator --it is an obj. that enables a programmer to traverse a container
print(f"this is the iterator that will iterate over the list1 = {my_iterator} and "
      f"id of my_iterator  in hex form is {hex(id(my_iterator))}")
n=1
while 1:

    try:
        print(f"{n} element of the list1 = {next(my_iterator)}")
        n+=1
    except StopIteration as x:
        print(x)
        break
print(n)'''



'''#aao ek charcha karte hai detail mein  jst to learn the behind the scene of   a line
#for i in my_list
class ListIterator:
    def __init__(self, lst):
        self._list = lst
        self._index = 0

    def __iter__(self):
        return iter(self._list)

    def __next__(self):
        if self._index < len(self._list):
            current_element = self._list[self._index]
            self._index += 1
            return current_element
        else:
            raise StopIteration()

# Example usage
my_list = [1, 2, 3, 4, 5]
my_iterator = ListIterator(my_list)

for item in ListIterator(my_list): #not in my_list
    print(item)

dekho yahan par aap for item in my_list hota which we write but what actually happens is that
for loop k wajah se my_list ka ek iterator banta hai which is my_iterator hai .............abb khud se padh
    lo'''


#we are writing the code to illustrate the behind the scene of this line that how it works
# for i in range (5):
class Iter:
    def __init__(self,n):
        self.n=n
    def __iter__(self):
        self.current=-1
        return self

    def __next__(self):
        self.current+=1
        if self.current>=self.n:
            raise StopIteration#this StopIteration will not get be printed on the console because
                                #n your code, the StopIteration exception is not being printed to the
            # console because the for loop is designed to handle StopIteration silently. When a Stop
            # Iteration exception is raised within the loop, it is caught and the loop terminates
            # gracefully without printing the exception.
        return self.current
x=Iter(5)
#for i in iter:
   # print(i)
'''here sabse pahle iter ka iterator banaya gaya hoga using __iter__  aur in this case iterable ka iterator khud
wahi iterator hi hai aur phir
dekho'''

iter1=iter(x) #yahan iter() explicitly call karna pada ...i hope u r getting it
i=next(iter1)
print(i)
i=next(iter1)
print(i)
i=next(iter1)
print(i)
i=next(iter1)
print(i)
i=next(iter1)
print(i)
'''same __next__() 5 baar  call hua hoga aur jb 6th time call hua hoga toh StopIteration aa gya aur u
if know aage ka'''