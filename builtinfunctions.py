#Built-In Functions + Methods
greet = "Helloooooo"
print(greet[0:len(greet)])
print(len(greet))

#String Methods: actions only strings can perform

quote = "to be or not to be"
print (quote.upper())
print(quote.capitalize())
print(quote.find('be'))
#finds the first occurance of a piece of text

print(quote.replace('be','me'))
print(quote)
#strings are immutable, we can overwrite them but we don't change them.

