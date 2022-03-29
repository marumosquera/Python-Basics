#Set
my_set={1,2,3,4,5,5}
print(my_set) #it only returns the unique values, no dupes.
my_set.add(100)
my_set.add(2)
print(my_set)

#Exercise: return a collection that returns only unique values

my_list = [1,2,2,3,4,5,5]
print(set(my_list))

#If we are getting the emails from a database, we don't want to have dupes and send multiple emails.
your_set = {4,5,6,7,2}
print(my_set.difference(your_set))
print(my_set.intersection(your_set))
print(my_set.union(your_set))
