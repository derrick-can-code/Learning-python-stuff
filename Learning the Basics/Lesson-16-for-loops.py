#for statements are used for iterating over a sequence, that is
#either a list, a tuple, a dictionary, a set, a string
fruits = ["apple", "banana", "pear"]
for x in fruits:
  print(x)
  
#range function allows us to start from default 0
for x in range(6):
  print(x)

#though default starts from 0, you could specify starting value too
for i in range(2, 6):
  print(i)
  
#it is also possible to specify an increment character by adding a third value for the increment
#provided I want to print odd numbers between 1 and 10
for x in range(1, 10, 2):
  print(x)