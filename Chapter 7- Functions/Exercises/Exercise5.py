## Exercise 5: Cities

def describe_city(city, country = 'italy'):
    msg = f"{city.title()} is located in {country.title()}."
    print (msg)

# To call function for three different cities
describe_city ('rome')
describe_city ('milan')
describe_city ('doha', 'qatar')
