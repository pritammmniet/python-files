#yeh bhi jaan lo phle
'''Here's a step-by-step explanation of how map() works:

When you call map() with a function and an iterable, it returns an iterator object that is capable of
generating the results.

The iterator object does not immediately compute and store all the results. It keeps track of the
function and the original iterable.

When you start iterating over the iterator object, it applies the function to the first item of the iterable
 and generates the result.

As you continue to iterate, the iterator applies the function to each subsequent item in the iterable and
generates the corresponding results one by one.

The generated results are made available to you during the iteration, allowing you to process them or
 store them as desired.

The iterator stops generating results once it has processed all the items in the iterable. At this point,
 the iteration is complete.


 In summary, squared_numbers is both an iterable and an iterator. It is an iterable because you can
  loop over it, and it is an iterator because it provides the __next__() method to retrieve the next
   item.
abb dekho in case of a  list ...list iterable hota hai aur iter(list) is that iterator that will iterate
over this list but in case of squared_numbers ...it is both as iter(squared_numbers) proves that it is
iterable and next(squared_numbers) proves ...it is iterator....hope u get it pritam...'''
numbers = [1, 2, 3, 4, 5,6,7,8,10,11,63]

squared_numbers = map(lambda x: x**2, numbers)
lstsn = list(map(lambda x: x**2, numbers))

print(squared_numbers) # Output: <map object at 0x...>

n=1
try:
    while 1:
        print(f"the {n} element of the squared_numbers is {next(squared_numbers)}")
        n+=1
except :
        print("Error")

#ek baat dekho yaha pe squared_numbers yahan pe iterator hai aur iterable bhi ...i will give a proof
import sys
print(f'The size of squared_numbers jst = {sys.getsizeof(squared_numbers)}')
print(f'The size of  list of squared_numbers  = {sys.getsizeof(lstsn)}')

