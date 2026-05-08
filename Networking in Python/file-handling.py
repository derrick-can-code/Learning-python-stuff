#open(file_path, mode) for opening a file. mode= read, write, append, etc 
file = open("file_1.txt", "r") #opens file in read mode, and return an object if file exists
print(file)
file.close() #ensures that files you write in or append something to saves the changes

#checking file properties
f = open("file_1.txt", "r")
print("File name:", f.name)
print("File mode:", f.mode)
print("Is closed?:", f.closed)
f.close()

#reading a file
f = open("file_1.txt", "r")
print(f.read())
f.close()

#writing a file in python
#when using with, file closes authomatically at the end of the block
with open("file_1.txt", "w") as file:
  file.write(" \"w\" mode opens the file for writing (overwrites existing content if the file already exists).")
  file.write("write() method adds new text to the file.")
  file.write("When using with, the file closes automatically at the end of the block.")
print("Success")

#handling exceptions when closing a file
try:
  file = open("geek.txt", "r")
  content = file.read()
  print(content)
except FileNotFoundError as e:
    print("Error:", e)
finally:
    file.close()