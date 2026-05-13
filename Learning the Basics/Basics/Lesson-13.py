a = 5
b = 15
if a > b:
  print("a is greater than b")
elif a == b:
  print("a is equal to b")
else:
  print("b is greater than a")

#ternary operator or shorthand if else
A = 32
B = 12
print("A") if a > b else print("B")

#it is possible to assign if else to a value
bigger = A if A > B else B
print("Bigger is", bigger)

#variable = value_if_true if condition else value_if_false

#ternary opeators are uselful for simple assignments and return statements
x = 15
y = 20
max_value = x if x > y else y
print("Maximum value is", max_value)

username = ""
display_username = username if username else "Guest"
print("Welcome,", display_username)

#python logical operators, and, or, not

#pass is used for development purposes
age = 16

if age < 18:
  pass # TODO: Add underage logic later
else:
  print("Access granted")