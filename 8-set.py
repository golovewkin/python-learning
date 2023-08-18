# Set is a collection which is unordered!!, unchangeable*, and unindexed. No duplicate members.
# * Note: Set items are unchangeable, but you can remove items and add new items.
# Duplicates Not Allowed Duplicate values will be ignored
myset = {"apple", "banana", "cherry"}
thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets

# Once a set is created, you cannot change its items, but you can add new items.
thisset2 = {"apple", "banana", "cherry"}
thisset2.add("orange")
print(thisset2)

# Add elements from tropical into thisset3:
thisset3 = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset3.update(tropical)
print(thisset3)  # {'cherry', 'banana', 'pineapple', 'mango', 'apple', 'papaya'}

# update method
thisset4 = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset4.update(mylist)
print(thisset4)  # {'banana', 'apple', 'kiwi', 'cherry', 'orange'}

# join 2 sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
# Note: Both union() and update() will exclude any duplicate items.!!!!
