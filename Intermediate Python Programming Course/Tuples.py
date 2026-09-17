# tuples cannot be changed, they are immutable. You cannot add or remove items from a tuple.
"""mytuple = tuple(["Max", 28, "Boston"]) # () is optional
print(mytuple) # prints the entire tuple

item = mytuple[1]
print(item) # prints the second item in the tuple

if "Max" in mytuple:
    print("Yes, 'Max' is in the tuple") # checks if an item is in the tuple
else:
    print("No, 'Max' is not in` the tuple")

mytuple = ("a", "p", "p", "l", "e")

print(mytuple.index("p"))
mylist = list(mytuple)
print(mylist)
mytuple2 = tuple(mylist)


#tuple slicing
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[2:5]
print(b) # prints (3, 4, 5), first index is inclusive, second index is exclusive


#unpacking tuples
mytuple = "Max", 28, "Boston"
name, age, city = mytuple # must match the number of items in the tuple
print(name) # prints Max
print(age) # prints 28
print(city) # prints Boston

mytuple = 0, 1, 2, 3, 4
i1, *i2, i3 = mytuple # *i2 will take all the items in the middle of the tuple
print(i1) # prints 0
print(i2) # prints [1, 2, 3]
print(i3) # prints 4

# difference between tuples and lists
import sys
mylist = [0, 1, 2, "hello", True]
mytuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(mylist), "bytes") # prints the size of the list in bytes
print(sys.getsizeof(mytuple), "bytes") # prints the size of the tuple in bytes
"""
import timeit
print(timeit.timeit(stmt="[0, 1, 2, 'hello', True]", number=1000000)) # prints the time it takes to create a list 1 million prints the time it takes to create a tuple 1 million times
print(timeit.timeit(stmt="(0, 1, 2, 'hello', True)", number=1000000)) # prints the time it takes to create a tuple