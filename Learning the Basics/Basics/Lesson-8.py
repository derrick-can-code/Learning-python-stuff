#for putting a value into a List
thisList = ["apple", "banana", "cherry"]
thisList.insert(2, "watermelon")
print(thisList)

#append items-add items to end of list
thisList.append("orange")
print(thisList)

#to append elements of another list to the current list, use the extend() keyword
tropical = ["Tree", "Forest"]

#adding elements of another List to the current list
#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.)
thisList.extend(tropical)
print(thisList)

#remove() \ specified item from a list
#however, when you have duplicates it removes the first occurence
thisList.remove("Tree")
print(thisList)

#pop is used to remove a specified index
thisList.pop(0)
print(thisList)

#however, if index isn't specified, pop removes the last item
thisList.pop()
print(thisList)

#del is also used like the op for removing specified index, but can however, also be used to delete the whole list
username = ["Kojo", "Clara", "Meroni", "Fafa", "Jigi"]
del username[0]
print(username)

#below, it deletes the whole list. Hence, the list name does not even exist after
#del username

#clear() , clears content of list
username.clear()
print(username)