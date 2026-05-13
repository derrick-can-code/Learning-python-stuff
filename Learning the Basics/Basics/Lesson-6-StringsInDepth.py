#txt.upper(), txt.lower(), txt.replace('H', 'J')
#txt.strip(), remove all spaces around

#The split() method splits the string into substrings if it finds instances of the separator:
#a = "Hello, World!"
#print(a.split(",")) # returns ['Hello', ' World!']

#String formats
#fStrings, the preferred way of formatting strings
#to specify f string, put f infront of the spring literal
age = 36
txt = f"My name is John. I am {age} years old"
print(txt)

#place holders and modifiers
price = 35.0
discount = 0.365 * price
print(f"You have a total discount of ${discount:.2f}")

#to insert illegal stuff, use an escape character
#escape character is basically a backslash \ followed by the stuff
print("He said to us, \"Come home and rest\"")