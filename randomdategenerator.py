import random
from datetime import datetime

year=random.randint(1900,2100)
month=random.randint(1,12)
day=random.randint(1,28)
hour=random.randint(0,23)
minute=random.randint(0,59)
second=random.randint(0,59)
random_date=datetime(year,month,day,hour,minute,second)
print (random_date)