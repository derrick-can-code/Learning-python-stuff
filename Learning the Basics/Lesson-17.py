def farenheit_to_celcius(fahrenheit):
  return (fahrenheit - 32) * 5/9

print(farenheit_to_celcius(77))

#functions have parameters(lname, fname), and arguments, actual name used when function is called
def greet(fname, lname):
  print("Hello", fname, lname)
greet("Derrick", "Mensah")

#default paramerers, so if there's no argument, default paramter iis used
def my_function(name = "friend"):
  print("My name is", name)

my_function()
my_function("Prince")

#You can combine regular parameters with *args.
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")