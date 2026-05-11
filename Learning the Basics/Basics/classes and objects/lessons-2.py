#Special methods
#they start with double underscores

class Cart:
  def __init__(self):
    self.items = []
    
  def add(self, item):
    self.items.append(item)
    
  def remove(self, item):
    if item in self.items:
      self.items.remove(item)
    else:
      print(f"{item} is not the cart")
      
  def list_items(self):
    return self.items
  
  def __len__(self):
    return len(self.items)
  
  def __getitem__(self, index):
    return self.items[index]
  
  def __contains__(self, item):
    return item in self.items
  
  def __iter__(self):
    return iter(self.items)
  
cart = Cart()
cart.add("Laptop")
cart.add('Wireless mouse')
cart.add('Ergo keyboard')
cart.add('Monitor')

for item in cart:
  print(item)
  
print(len(cart))
print(cart[3])

print("banana" in cart)
cart.remove("Ergo keyword")

print(cart.list_items())