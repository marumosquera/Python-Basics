is_old = True
is_licenced = True

if is_old and is_licenced:
    print('you are old enough to drive!')

else:
    print('you are not of age')

print('out of if')

#Ternary Operator
# confition_if_true if  condition else confition_if_else
is_friend = True
can_message = 'message allowed' if is_friend else 'not allowed to message'

print (can_message)

#Short Circuiting
is_Friend = True
is_User = True

if is_Friend or is_User:
  print('best friends forever')
#short circuiting happens when the interpreter understands that if the first condition before the "or" is already true, then it doesn't care about the 2nd condition. Because either way is printing 'best friends forever'. Same happens if before the "and" you have a "false".
#We want our machines to be efficient


