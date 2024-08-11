day=(input("enter the date:"))
month=(input("enter the month:"))
year=(input("enetr the year:"))
date=day+month+year
rev_date=date[::-1]
if date==rev_date:
    print("palin date")
else:
    print("not")
                