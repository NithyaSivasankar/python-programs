date=int(input("enter the date:"))
month=int(input("enter the month:"))
year=int(input("enetr the year:"))
if year in range(0,2025):
    if month>12:
        print(month,"not valid")
    else:
        if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
            if date in range(1,32):
                print(date,month,year,"valid")
            else:
                print(date,month,year,"not valid")
        elif month==2:
            if year%400==0 or year%4==0 and year%100!=0:
                if date in range(1,30):
                    print(date,month,year,"valid")
                else:
                    print(date,month,year,"not valid")
            else:
                if date in range(1,29):
                    print(date,month,year,"valid")
                else:
                    print(date,month,year,"not valid")
        else:
            if date in range(1,31):
                print(date,month,year,"valid")
            else:
                print(date,month,year,"not valid")
else:
    print(year,"not valid")