# definition
my_list = [1]


# example with default arguments
def greet(cb, name='Denys', my_list=None):
    print('hello')
    print(my_list)  # access to the my list
    print(name)
    if cb is None:
        print('!!')
    else:
        cb(name)


def cb(name):
    print(name)


greet(cb)


# it ignores the second function definition
# def greet():
#     print(1)

# skip arguments example
def print_names(first_name, _, last_name):
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")


print_names("John", None, "Doe")
