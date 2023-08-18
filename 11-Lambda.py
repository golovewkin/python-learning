# A lambda function is a small anonymous function
x = lambda a: a + 10
print(x(5))


def myfunc(n):
    return lambda a: a * n
