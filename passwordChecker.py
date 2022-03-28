#How many characters has the password?
username= input('Please introduce your user:')
password= input('Please create a password:')
passwordlength = len(password)
secret = '*' * passwordlength

print(f'{username}, your password {secret} is {passwordlength} letters long')

