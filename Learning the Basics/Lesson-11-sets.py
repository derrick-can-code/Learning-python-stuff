#sets are unordered, immutable, do not allow duplicates

mySet =  {"apple", "banana", "cherry", "apple"}
print(mySet)

#they cannot be indexed, because anytime you call them, they tend to have different orders or arrangeents

#true and 1, considered same values
#false and 0, considered same values
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)


#once a set is created, you cannot change its items but you can addd new items
thisset.add("orange")
print(thisset)

#to add items to current set from another set, use the update method
#object in update can be any iterable(tuple, set, list, dictionaries)
newSet = ("Goat", "Cow", "Fish")
thisset.update(newSet)
print(thisset) 

#several ways to join sets
#The union() and update() methods joins all items from both sets.
#The intersection() method keeps ONLY the duplicates.
#The difference() method keeps the items from the first set that are not in the other set(s).
#The symmetric_difference() method keeps all items EXCEPT the duplicates.

#union or |
set1 = {"a", "b", "c", 1, 3}
set2 = {1, 2, 3, 4, 5, 6, "b"}
set3 = set1.union(set2)
set4 = set1 | set2
print(set3)
print(set4)

#joining multiple sets, just separate with a comma
set5 = {"Goat", "Cow"}
set6 = set1.union(set2, set3, set5)
print(set6)

#update, allows you to update the original set instead of returning a new one
set5.update(thisset)
print(set5)

# | allows sets to sets, whiles union allows sets with other data types

#intersection returns the duplicates. &
#intersection_update(), used the same way as the update() method


#difference, or -
#difference_update()
#returns items in first set, not in the second set

#symmetric_difference


#frozensets, just like sets, however, elements cannot ve added or removed from the set
x1 = frozenset({"apple", "pear"})
print(x1)