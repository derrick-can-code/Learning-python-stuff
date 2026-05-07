#regex, basically cool ways to go about extracting data
import re
#practing with ReGex and files, let's try something

#create the text we are going to put in our file
user_data = """
    Alice   |  alice@email.com  |  User_123   
   Bob | bob@web.com | Admin_456   
     Charlie | charlie@site.org | Guest_789  
"""

#we create a file, make it writable, and we put the user_data into it
with open("user_file.txt", "w") as file:
  file.write(user_data)
  
user_email = []

#read the file
with open("user_file.txt", "r") as text:
  for line in text:
    line = line.strip()
    email = re.findall(r'\S+@\S+', line)
    
    if email:
      user_email.append(email[0])
  
print(user_email)