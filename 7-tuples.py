# A tuple is a collection which is ordered and unchangeable and allow duplicate values !!!!
my_tuple = ("apple", "banana", "cherry", "apple", "cherry")
my_tuple2 = tuple(("apple", "banana", "cherry", "apple", "cherry"))  # the same
print(my_tuple)
print(my_tuple2)

print(len(my_tuple))

# one item in tuple is not a tuple
thistuple = ("apple",)
print(type(thistuple))  # <class 'tuple'>

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))  # <class 'str'>

# can be any data type
tuple_any = ("abc", 34, True, 40, "male")

# get the second last item
print(tuple_any[-2])  # 40
# using range
print(tuple_any[2:5])

# check if item exists
if "apple" in tuple_any:
    print("Yes, 'apple' is in the tuple_any")

# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
# any actions you can do with lists you can do with tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# "packing" a tuple (creation)
fruits = ("apple", "banana", "cherry")
# unpacking
(green, yellow, red1) = fruits
print(green)  # apple
(green, yellow2, *red) = fruits  # rest operator?
# Python will assign values to the variable until the number of values left matches the number of variables left.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green3, *tropic, red3) = fruits
print(green3)  # apple
print(tropic)  # ['mango', 'papaya', 'pineapple']
print(red3)  # cherry

# Loop Through the Index Numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

    # using while
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

# Tuple methods
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found Methods
