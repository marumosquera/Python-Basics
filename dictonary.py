#Dictonary
dictonary = {
  'a':[1,2,3],
  'b':'hello',
  'c': True
}

print(dictonary['a'][1])

#my list contains a dictonary
my_list=[
  {
  'a':[1,2,3],
  'b':'hello',
  'c': True
  },
  {
  'a':[4,5,6],
  'b':'hello',
  'c': False
  }
]

print(my_list[0]['a'][1])

#a dictonary key has to be immutable, can't be a list.

user={
  'basket': [1,2,3],
  'greet': 'hello',
  'age':34
}

print(user.get('age',55)) #In case there isn't a "age" in the dict, will return 55. If not, it returns the value from the dict
#Helps to avoid error

#I can check keys and values from the dict
print('hello' in user.keys()) #false
print('hello' in user.values()) #true

user2= user.copy()
user.clear()
print(user)
print(user2)
print(user2.pop('age'))