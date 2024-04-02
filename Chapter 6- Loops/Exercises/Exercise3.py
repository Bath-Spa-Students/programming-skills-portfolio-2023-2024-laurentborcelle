## Exercise 3: Infinity


# Infinite loop execution
while True:

    age = input("Enter your age: ") # Age indication of user
    
    age = int(age)
    if age < 3:
        print ("Your ticket is free.")
    elif age < 13:
        print ("The ticket costs $10.")
    else:
        print ("The ticket costs $15.")
    

    