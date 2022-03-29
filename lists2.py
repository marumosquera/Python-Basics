basket = [1,2,3,4,5]

#adding
basket.append(100)
#after appending then we can assign

basket.insert(2,99)
print(basket)

#removing methods
basket.pop(0) #removes the index
basket.remove(4) #removes the value
print(basket)
new_list = basket.pop(2)
print(new_list) #still returns something

new_list2= basket.clear() #removes whatever is in the list
print(basket)

my_basket = ['a','x','b','c','d','e']
print(my_basket.index('d',0,6))
print('d' in my_basket)
print('i' in 'hi, how are you?')
print(my_basket.count('d'))

my_basket.reverse()
print(my_basket)

print(list(range(1,100))) #great way to generate a list super quickly

sentence= ' '
new_sentence= sentence.join(['hi','my','name','is','Eli'])

print(new_sentence) #combining list into a string

#List Unpacking

a,b,c,*other, d=[1,2,3,4,5,6,7,8,9]
print(b)
print(other) #I'm able to unpack my list
print(d)

#None - represents the absence of Value

weapons = None
print(weapons)

