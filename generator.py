'''#extra note hai
range() mere acc. ek list ka replacement hai jb hume iterate karna hota hai ...for example range(1,11) pe
iterate karo ya list=[1,2,3,4,5,6,7,8,9,10] pe baat same hai with only diffn that list ko apne saare elements
store karne k liye jyada memory chayiye as compared to range jo store karta hai start,end , step ....baat
need ki hai ..samjhe
#code
import sys
list=[1,2,3,4,5,6,7,8,9,10]
print(f"the size of list is {sys.getsizeof(list)}")
print(f"the size of range(1,11) is {sys.getsizeof(range(1,11))}")'''

'''A generator in Python is a special type of iterator that generates values on-the-fly. It allows you to 
iterate over a sequence of values without the need to store them in memory all at once. Generators are
 defined using a special syntax that includes the yield keyword.

Here's an example of a simple generator function that generates a sequence of numbers:'''
def number_generator(n):
    for i in range(n):
        yield i

# Using the generator

for num in number_generator(5):
    print(num)
#note one thing that here number_generator(5) is both iterable and iterator like x=map(a1,a2)
#dekho upar example  mein yahan num = number_generator(5) bs yeh rhs wali value return k barabar hota hai
# but yeh value  wah  yield dega ...dekho baat yeh hai ki jaise yeild hit hota hai waise hi function wahi
#ruk jata hai aur number_generator(5) iski value yield de raha hota hai ..phir  number_generator  resume hota
#hain to yield the next value and given back for the num ...so this is how it works


#now understand this code to get the depth
def gen():
    yield 1
    print("pause 1")
    yield 2
    print("pause 2")
    yield 3
    print("pause 3")
    yield 4
    print("pause 4")
x=gen()#here the gen is not called ...weird?? then research
y=iter(x) # u can use x in place of y it will work the same as x is already an iterator here using iter()
# we want to show x is iterable too
print(next(y))
print(next(y))
print(next(y))
print(next(y))
#this print("pause 4") was never printed



