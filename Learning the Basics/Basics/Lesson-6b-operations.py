x = 15
y = 4
print(x // y) #floor division
print(x ** y) #exponential stuff

#Walrus operator, print(x:= 3), same as x = 3, print(x)
#so basically, works everything out, and stores it in the value

numbers = [1, 2, 4, 5, 6, 7]
if(count:= len(numbers)) >3:
  print(f"List has {count} numbers")
  
#logical operators, and and or, are used between two conditional statements
x = 5
print(x > 0 and x < 10)
print(x > 0 or x < 10)
print(not(x > 0 and x < 10))

#Identity operators
#both is and is not is used to check whether two variables point in the same location in memory
#difference between == and is, is that, is checks for pointing of memory location, whereas == checks whether the variables are the same

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x == y)
print(x is y)
print(x is z)
print(x is not y)