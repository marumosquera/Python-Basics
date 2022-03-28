list = [1,2,3,4,5]
list2 = ['a','b','c']

amazon_cart= ['notebooks','sunglasses'] #we can add diff data, and we can access to it in diff ways.

print(amazon_cart[1])
#sunglasses

#List Slicing
amazon_cart1= ['notebooks','sunglasses','toys','grapes']
print(amazon_cart[0::2])
#Lists are mutable 

amazon_cart1[0] = 'laptop'
new_cart = amazon_cart1[0:3]
print(amazon_cart1) #I'm able to change the list
print(new_cart)

#If I do new_cart = amazon_cart and then new_cart[0]='gum' I'm changing amazon cart too... If I don't want to do that I need to do new_cart = amazon_cart[:]

#Matrix - this comes up a lot in Machine Learning or Image Processing 
matrix= [
  [1,2,3],
  [2,4,6],
  [4,8,9],
]

#A computer can understand an image through pixels on the screen, we can have them as 0 and 1.

print(matrix[0][1]) #access the first item, and then grabs the second item in that first array.


