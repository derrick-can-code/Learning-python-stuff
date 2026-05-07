import re

num_list = []

with open("regex_sum_42.txt", "r") as file:
  for line in file:
    num_str = re.findall('[0-9]+', line)
    
    if num_str:
      num_list.extend(num_str)
      
print(num_list)
print(len(num_list))

num_sum = 0

for num in num_list:
  new_num = int(num)
  
  num_sum += new_num
print(num_sum)