#*args and **kwargs allow functions to accept a unknown number of arguments.
#args are useful when you're trying to create flexible functions
#regular functions must come before args
def sum_of_values(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total 

print(sum_of_values(1, 2, 3))

def max_value(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(max_value(3, 7, 2, 9, 1))

#Using **kwargs to accept any number of keyword arguments:
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#Accessing values from **kwargs:
def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")

#you could also combine regular arguments with kwargs
def user(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)
    
user("emil123", age = 25, city = "Oslo", hobby = "coding")