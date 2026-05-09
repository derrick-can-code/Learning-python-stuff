def modify(a):
  a += 10
  return a
x = 5
print(modify(x))
print(x)


def modify(lst):
  lst.append(10)
  return lst

list = [2, 4]
modify(list)
print(list)