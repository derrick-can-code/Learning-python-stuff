thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
for i in range(len(thislist)):
  print(thislist[i])
  
  
names = ["Derrick", "John", "James", "Paul", "Freddricka"]
i = 0
while i < len(names):
  print(names[i])
  i += 1
  
#looping using list comprehension
[print(x) for x in names]
1

#list comprehension offers a synatx for creating a new list based on an existing one
fruits =  ["apple", "banana", "cherry", "kiwi", "mango"]
newList = [x for x in fruits if "a" in x]
print(newList)

#newlist = [expression for item in iterable if condition == True]

#by default, sorts in ascending order, from lowest to highest
fruits.sort()
print(fruits)

list = [x for x in range(10)]
print(list)

#making it descending order
list.sort(reverse = True)
print(list)


def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


#Reverse the order of the list items:
thislist1 = ["banana", "Orange", "Kiwi", "cherry"]
thislist1.reverse()
print(thislist1)

#copying a list
mylist = thislist1.copy()
print(mylist)

#joining lists
#by using the + operator
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list2 + list1
print(list3)