x = range(6)
for n in x:
    print(n)

tuple_any = ("abc", 34, True, 40, "male")
print(tuple_any[2:5])  # from 2 to 5
print(tuple_any[:4])  # from 0 to 4
print(tuple_any[2:])  # from 2 to the end
# can be negative
print(tuple_any[-4:-1])
