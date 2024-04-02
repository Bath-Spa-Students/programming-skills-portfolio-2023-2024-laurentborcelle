## Exercise 4: Deli

# Create a list of preferred types of sandwiches for the order
sandwich_orders = ['Reuben', 'Turkey Ham', 'Club', 'Grilled','Chickenburger', 'Croque monsieur', 'Bagel']

# Proceed to create an empty list
finished_sandwiches = []

print ("\nAs per your request: ") # An introductory message
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print (f"\n Your {current_sandwich} sandwich is currently being prepared.")
    finished_sandwiches.append(current_sandwich)

print ("\n\n")
print ("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print (f" - {sandwich}")
 
# Print message for each completed sandwich 
print ("\n")
print ("!! 𝙳𝙸𝙽𝙶 𝙳𝙸𝙽𝙶 𝙳𝙸𝙽𝙶 !!")
for sandwich in finished_sandwiches:
    print (f"\n Your {sandwich} sandwich is ready to be served.")
print ("\n")