# Dictionary is a collection which is ordered** and changeable. No duplicate members.
# **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
# thisdict = dict(name = "John", age = 36, country = "Norway") another way to create
print(thisdict["brand"])

# has methods
x = thisdict.get("model")
x2 = thisdict.keys()
x3 = thisdict.values()
x4 = thisdict.items()

# how to copy dict
mydict = thisdict.copy()
mydict2 = dict(thisdict)

# how to add an elem
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"color": "red"})
