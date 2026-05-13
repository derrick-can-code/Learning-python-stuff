#elsle statement can be used in conjunction with the while statement
i = 1
while i < 6:
  print(i)
  i += 1
else: 
  print("i is no longer less than 6")

#break, allows us to exit a statement
#example, when i is 3, break out of the statement
j = 1
while j < 6:
  print(j)
  if j == 3:
    break
  j += 1
  
#continue, allows you to skip