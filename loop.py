#Exercise: Tricky Counter

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counter = 0

for item in my_list:
    counter = counter + item

print(counter)

#I'm going to loop 2 times, the object below
for num in range(2):
    print(list(range(10)))

for i,char in enumerate(list(range(100))):
  if char == 50:
    print(f'index of 50 is:{i}')