## Exercise 3: Print Date and Time 

# DATE
from datetime import date
today = (date.today())
d = today.strftime ("%B %d, %Y")
print ("DATE TODAY:", d)

# TIME
from datetime import datetime
now = datetime.now()
t = now.strftime ("%H:%M:%S")
print ("CURRENT TIME:", t)
