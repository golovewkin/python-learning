# Arbitrary Arguments, *args
def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


# Keyword arguments. works with any sequence
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child3="Emil", child1="Tobias", child2="Linus")


# Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")


# Default Parameter Value
def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")


# Empty one
def myfunction():
    pass
