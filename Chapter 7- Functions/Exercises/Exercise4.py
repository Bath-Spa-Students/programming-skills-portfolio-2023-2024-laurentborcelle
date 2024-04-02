## Exercise 4:  Large Shirts

# The shirt is set to large as the default size
def make_shirt(size = 'large', msg = 'I love Python.'):
    print (f"\nI am going to tailor a {size} shirt.")
    print (f'The shirt shall read, "{msg}"')

# Function for additional sizes and a message
make_shirt()
make_shirt (size = 'medium')
make_shirt ('small', 'Python is basic.')
print ("\n")