#dictionaries, store values using key-value pairs
#dictionaries are ordered, changeable, do not allow duplicates
thisdict = {"brand": "toyota",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#dictionaries can have values of any data type
#however, you cannot have duplicate keys
myCar = {
  "name": "Ford",
  "isNew": True, 
  "Amount": "$500",
  "colors" : ["red", "blue", "white"]
}
print(myCar)
print(myCar["name"]) #access items by referring to key names 
#alt for above is, myCar.get("name")

#keys(): view of the dictionary
x = myCar.keys()
print(x) #before change
myCar["year"] = 1965
print(x) #after

#values(), returns the list of values in the dictionary

#items, return each item as a tuple
x = myCar.items()
print(x)