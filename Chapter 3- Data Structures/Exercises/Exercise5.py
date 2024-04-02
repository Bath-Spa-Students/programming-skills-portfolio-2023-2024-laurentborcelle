## Exercise 5: Change Guest List



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


# Specified guest unable to attend
name = myguest_list[-3].title()
print ("\nIt is our sincerest apologies that " + name + " is unable to make it to dinner.")

# Guest replacement modification
del (myguest_list[-3])
myguest_list.insert (-4, 'Emporio Armani')

#  Second invitation set list for remaining guests
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


