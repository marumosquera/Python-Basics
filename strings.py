#Strings

print(type("hi hello there!"))
username = 'supercoder'
password = 'super secret'
long_string= '''
WOW
o o
---
'''

print(long_string)

first_name= "Elisa"
last_name= "Mosquera"
full_name = first_name + ' ' + last_name
print(full_name)

#string concatenation
print('hello ' + full_name)

#Type Conversion
print(type(int(str(100))))

a= str(100)
b = int(a)
c = type(b)
print(c)

#Escape Sequence
weather= "\t It\'s \"kind of\" sunny \n hope you have a good day!"
print(weather)

#   It's "kind of" sunny 
# hope you have a good day!

#Formatted strings
name = "Johnny"
age = 55
print('hi ' + name + '. You are ' + str(age) + ' years old')
#new in Python 3
print(f'hi {name}. You are {age} years old')

#Python 2
print('hi {}. You are {} years old'.format('Johnny','55'))

print('hi {1}. You are {0} years old'.format(age, name))

#String indexes
selfish = '01234567'
        #  01234567

# [start:stop:stepover] 
print(selfish[0:8:2])
#0246
print(selfish[::-1])
#76543210

