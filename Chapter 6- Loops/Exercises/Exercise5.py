## Exercise 5: No Pastrami

# Create a list of preferred types of sandwiches for the order
sandwich_orders = ['Pastrami', 'Reuben', 'Turkey Ham', 'Club', 'Grilled', 'Chickenburger', 'Pastrami', 'Croque monsieur', 'Bagel', 'Pastrami']

# Proceed to create an empty list
finished_sandwiches = []

print ("\nIt is our sincerest apologies that the deli has ran out of pastrami.")
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

print ("\n")
print ("On the meanwhile:")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print (f"\n Your {current_sandwich} sandwich is currently being prepared.")
    finished_sandwiches.append(current_sandwich)

print ("\n")
print ("!! 𝙳𝙸𝙽𝙶 𝙳𝙸𝙽𝙶 𝙳𝙸𝙽𝙶 !!")
# Print message for each remaining completed sandwich 
for sandwich in finished_sandwiches:
    print (f"\n Your {sandwich} sandwich is ready to be served.")
print ("\n")