'''
Name: Ruby Koehler
Date: 10/22/24
Description: Unit 2 & 3 Seasons Project
'''

user_month = input("Enter the name of the month: ")
day = int(input("Enter the day (1-31): "))
month = user_month.title()

if month == 'March' and (20 <= day <= 31):
    print(f"{month} {day} is in Spring")
elif month == 'March' and day < 20:
    print(f"{month} {day} is in Winter")
elif month == 'June' and (21 <= day <= 30):
    print(f"{month} {day} is in Summer")
elif month == 'June' and day < 21:
    print(f"{month} {day} is in Spring")
elif month == 'September' and (22 <= day <= 30):
    print(f"{month} {day} is in Fall")
elif month == 'September' and day < 22:
    print(f"{month} {day} is in Summer")
elif month == 'December' and (21 <= day <= 31):
    print(f"{month} {day} is in Winter")

elif month == 'December' and day < 21:
    print(f"{month} {day} is in Fall")
elif month == 'April' and day <= 30:
    print(f"{month} {day} is in Spring")
elif month == 'May' and day <= 31:
    print(f"{month} {day} is in Spring")
elif (month == 'July' or month == 'August') and day <= 31:
    print(f"{month} {day} is in Summer")
elif month == 'October' and day <= 31:
    print(f"{month} {day} is in Fall")
elif month == 'November' and day <= 30:
    print(f"{month} {day} is in Fall")
elif month == 'January' and day <= 31:
    print(f"{month} {day} is in Winter")
elif month == 'February' and day <= 28:
    print(f"{month} {day} is in Winter")
else:
    print(f"{month} {day} is not in our calendar; please input a real date.")