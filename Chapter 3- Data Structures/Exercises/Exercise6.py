# Exercise 5: Change Guest List



myguest_list = ['Byredo', 'Carolina Herrera', 'Jo Malone', 'Maison Margiela', 'Narciso Rodriguez']

name = myguest_list[0].title()
print (name + ", we are most delighted to invite you over for dinner.\n")

name = myguest_list[1].title()
print (name + ", we are most delighted to invite you over for dinner.\n")

name = myguest_list[2].title()
print (name + ", we are most delighted to invite you over for dinner.\n")

name = myguest_list[3].title()
print (name + ", we are most delighted to invite you over for dinner.\n")

name = myguest_list[4].title()
print (name + ", we are most delighted to invite you over for dinner.\n")

name = myguest_list[-3].title()
print ("\nIt is our sincerest apologies that " + name + " is unable to make it to dinner.")

del (myguest_list[-3])
myguest_list.insert (-4, 'Emporio Armani')

name = myguest_list[0].title()
print ("\n" + name + ", we are most delighted to invite you over for dinner.\n")

name = myguest_list[1].title()
print (name + ", we are pleased to invite you over for dinner.\n")

name = myguest_list[2].title()
print (name + ", we are pleased to invite you over for dinner.\n")

name = myguest_list[3].title()
print (name + ", we are pleased to invite you over for dinner.\n")

name = myguest_list[4].title()
print (name + ", we are pleased to invite you over for dinner.\n")

# Shrinkage of myguest_list

print ("\nIt is our sincerest apologies, however, we are only able to invite two people over for dinner.\n")

name = myguest_list.pop()
print ("\nIt is our sincerest apologies, " + name.title() + " there is no longer any room at the table.\n")

name = myguest_list.pop()
print ("\nIt is our sincerest apologies, " + name.title() + ", there is deplorably no longer any room at the table.\n")

name = myguest_list.pop()
print ("\nIt is our sincerest apologies, " + name.title() + ", there is deplorably no longer any room at the table.\n")

name = myguest_list[0].title()
print (name + ", we are pleased to invite you over for dinner nonetheless.\n")

name = myguest_list[1].title()
print (name + ", we are pleased to invite you over for dinner nonetheless.\n")

print ('Though, eventually..\n')

del (myguest_list[0])
del (myguest_list[0])

print ('The current names in the guest list are:',myguest_list)


