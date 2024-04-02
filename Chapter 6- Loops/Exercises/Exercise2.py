## Exercise 2: Movie Tickets

# Prompt customer instructions
prompt = "\nEnter your age."

prompt += "\nEnter [quit] when you are finished: "

# Loop execution
while True:
    
    customer_age = input(prompt)
    if customer_age == 'quit':
        break
    customer_age = int(customer_age)

    if customer_age < 3:
        print ("Your ticket is free.")
    elif customer_age < 13:
        print ("The ticket is at the cost of $10.")
    else:
        print ("The ticket is at the cost of $15.")