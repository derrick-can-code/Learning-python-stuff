#Lists are ordered, changeable, allows duplicates

#Python tuples
#Unlike lists, we use circular brackets around them
#they are ordered, allows duplicates, but unchangeable
thistuple = ("apple", "banana", "orange")
print(thistuple)

#to create a tuple with one item
singletuple = ("boy",) #always remember the comma
print(singletuple)

#creating a tuple using the tuple() constructor
mytuple = tuple(("car", "mantion", "fan"))
print(mytuple)

#tuples are immutable or unchangeable, hence if you want to change them, you have 
#to change the tuple into a list first
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "milk"
x = tuple(y)
print(x)

#you can add tuples to tuples

#del can be used to permanently delete a tuple

#unpacking a tuple
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)