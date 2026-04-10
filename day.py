from datetime import datetime
date_input=input("Enter a date(YYYY-MM-DD): ")
date_object=datetime.strptime(date_input,"%Y-%m-%d")
day=date_object.strftime("%A")
print (day)