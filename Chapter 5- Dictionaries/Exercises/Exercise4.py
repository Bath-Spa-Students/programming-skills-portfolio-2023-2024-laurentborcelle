## Exercise 4: Rivers 


major_rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Yangtze': 'China',
    }

for river, country in major_rivers.items():
    print ("\nThe " + river.title() + " flows through " + country.title() + ".")

print ("\nThe following major rivers are included in this list:")
for river in major_rivers.keys():
    print ("- " + river.title())

print ("\nThe following countries the rivers are located in include:")
for country in major_rivers.values():
    print ("- " + country.title())