#Tuples
my_tuple = (1,2,3,4,5)
print(my_tuple)
print(5 in my_tuple)
#it's immutable

#Benefits: if you don't need to change the list, it tells other programmers it won't be change. Makes code more predictable. Less flexible, and faster. 

#Good use of a tuple: geographic location. Pick up point. 
#But when the car is moving, we need a list. It's changing.

#for tuples () for lists []

new_tuple = my_tuple[1:2]
print(new_tuple)
print(len(my_tuple))