## Exercise 1: Pizza Toppings

prompt = "\nIndicate the topping of choice on your pizza."

prompt += "\nEnter [quit] after choosing all your toppings: "

while True:
    
    pizzatopping = input(prompt)
    if pizzatopping != 'quit':
        print (" The " + pizzatopping + " will be added to your pizza.")
    else:
        break
