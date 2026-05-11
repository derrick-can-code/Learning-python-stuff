#to define a class, just use the class keyword infront of it
#then within the class, we add an initializer along with any attributes or methods
class Dog:
  species = "French Bull dog" #instance attributes
  
  def __init__(self, name, age): #class attributes
    self.name = name
    self.age = age
    
  def bark(self):
    print(f"{self.name.upper()} says woof woof!")

print(Dog.species)
    
dog_1 = Dog("German Shepperd", "22")
dog_2 = Dog("Wild wolf", "14")

dog_1.bark()
dog_2.bark()