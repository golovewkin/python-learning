is_old = True  # boolean
string = 'Denys'  # strings
number = -1.2  # numbers

# numbers
print(1_000_000)  # 1000000 - interesting
print(1 / 3)  # 0.3333333333333333
print(0.1 + 0.2)  # 0.30000000000000004 - hahaha

# coercion
# print(int(is_old) + int(name))  # error
print(int(1.3))  # 1
print(int(True))  # 1
print(int(False))  # 0
print(bool(string))  # True
print(bool(number))  # True
print(float(number))  # -1.2
# print(float(string))  # error

# strings base
print('hello ' + 'word')  # hello word
# print('hello ' * 'word')  # hello word - Cannot do it
print('hello ' * 10)  # hello hello hello hello hello hello hello hello hello hello
print("I'm pretty cool")
print('I\'m pretty cool')
print("""hello 
multiple lines text""")
