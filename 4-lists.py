# Actually these are arrays in JS
example_list = [1, '22']
# print(example_list[2]) error
# many methods similar to JS
print(example_list)
example_list.append(True)
print(example_list)
print(len(example_list))  # how to get length
# get last value
print(example_list[-1])

# using function
thislist = list(("apple", "banana", "cherry"))  # note the double round-brackets
for example in thislist:
    print(example)

# check if elem in list
print('apple' in thislist)
print('apple2' in thislist)

# shortcuts
# The return value is a new list, leaving the old list unchanged
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]  # newlist = [expression for item in iterable if condition == True]
print(newlist)

# how to copy array
copy_of_fruits = [x for x in fruits]
print(copy_of_fruits)

# sort list
thislist.sort()

# copy list
# 1 way
thislist.copy()
# 2 way
fruitslist = ["apple", "banana", "cherry"]
fruitslistCopy = list(fruitslist)
print(fruitslistCopy)

# join lists
print(fruitslist + fruitslist)

# how to add an element
fruits.append('kiwi')
fruits.insert(1, 'cherry')

# how to remove an element
fruits.remove("kiwi")

# print a range of elements
print(fruits[2:5])
