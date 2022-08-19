import calendar
import datetime

dateNow = datetime.datetime.now()
year = dateNow.year
month = dateNow.month
day = int(input("When is your next shift (day)?: "))
nextYear = year + 1
date = datetime.date(year, month, day)
date_list=[]
query_year = int(input("Insert selected year: "))
query_month = int(input("Insert selected month: "))
query_day = int(input("Insert selected day: "))
my_shift = datetime.date(query_year, query_month, query_day)

wanted_shift = calendar.weekday(query_year,query_month,query_day)
yearCount = int(365 / 5)

def correct_month(current_month):
    if dateNow.day <= day:
        return month
    else:
        return month + 1

date = datetime.date(year, correct_month(day), day)
date_list=[date + datetime.timedelta(days=5)]

for x in range(yearCount):
    date += datetime.timedelta(days=5)
    date_list.append(date)

def weekDay(finalDate):
    if finalDate == 0:
        return "Monday"
    if finalDate == 1:
        return "Tuesday"
    if finalDate == 2:
        return "Wednesday"
    if finalDate == 3:
        return "Thursday"
    if finalDate == 4:
        return "Friday"
    if finalDate == 5:
        return "Saturday"
    if finalDate == 6:
        return "Sunday"

def shift(date):
    if my_shift in date_list:
        return ("\nIn %s, %s, you have day-shift."%(my_shift,weekDay(wanted_shift)))
    elif my_shift-datetime.timedelta(days=1) in date_list:
        return ("\n%s, %s,you have night-shift."%(my_shift,weekDay(wanted_shift)))
    elif my_shift-datetime.timedelta(days=2) in date_list:
        return ("\n%s, %s, you will be after night-shift."%(my_shift,weekDay(wanted_shift)))
    elif my_shift-datetime.timedelta(days=3) in date_list:
        return ("\n%s, %s, you have 1. free day."%(my_shift,weekDay(wanted_shift)))
    elif my_shift-datetime.timedelta(days=4) in date_list:
        return ("%s, %s, you have 2. free day." % (my_shift, weekDay(wanted_shift)))
    else:
        return "UNKNOWN ERROR!"
print(shift(date))

print("You wish to show a list of all shifts\n")
yn = input("Insert Y for YES, or N for NO: ")
print()

date = datetime.date(year, month, day)
if yn == "y" or yn == "Y":
    for i in range(yearCount):
        while date < datetime.date(nextYear, 3, 1):
            date += datetime.timedelta(days=5)
            dateY = int(date.strftime("%Y"))
            dateM = int(date.strftime("%m"))
            dateD = int(date.strftime("%d"))
            finalDate = calendar.weekday(dateY,dateM,dateD)
            print(date, end= ", {}, you have day-shift\n".format(weekDay(finalDate)))
            print(date+datetime.timedelta(days=1),
                  end=", {}, you are before the night-shift \n".format(weekDay(finalDate+1)))
            print(date+datetime.timedelta(days=2),
                  end=", {}, you are after the night-shift\n".format(weekDay(finalDate+2)))
            print()

    print("These are all shifts until March next year..")
elif yn == "n" or yn == "N":
    print("Thank you, goodbye")
else:
    print("Wrong choice, goodbye!")
