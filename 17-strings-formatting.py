quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# with index numbers
# if you want to refer to the same value more than once, use the index number
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Named Indexes
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Ford", model="Mustang"))
