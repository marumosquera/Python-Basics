is_magician = False
is_expert = True

#check if magiciand AND expert: 'You are a master magician'
#check if magician but not expert: 'at least you're getting there'
# if you are not a magician: 'you need magic powers'

if is_magician and is_expert:
  print('Your are a master magician')
elif is_magician and not is_expert:
  print('at least you are getting there')
elif not is_magician: 
  print('you need magic powers')

