#just assign a value and you have created a variable
x=20
print(x)

#casting
#done by wraping around the data type around the value
x= str(3)
y = int(3)
z = float(3)

print(x, y) #gives you 3 3, since x is a string. Strings can't be added to ints
print(y+z)

#use type for finding datatype
print(type(x))
print(type(y))
print(type(z))

#python allows multiple assignment
x,y,z= "Orange", "Banana", "Cherry"
print(x, y, z)

#unpacking collections
fruits = ["Pear", "Orange", "Avocado"]
x, y, z = fruits
print(x, y, z)

#global variable x is used outside
#local x is used inside.
#in functions, the local variable would always override the global one if you reassign
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()
print(x)

#to use the local a outside, we add global to it
def myfunc1():
  global a 
  a = "fantastic"

print("Python is " + a)
print("Python is " + a)
print(a)
