# Import modulov
import calendar
import datetime
from tkinter import *

# VLASTNÉ FUNCIE:
# Zistí či sa môže jednať o mesiac nasledujúci
def correct_month(input_day):
    if date_today.day < next_shift:
        return month_today
    else:
        answer__next_month = input("Jedná sa o nasledujúci mesiac?: ")
        if answer__next_month == "a" or answer__next_month == "A":
            return month_today + 1
        else:
            return month_today

# Výpis správneho dňa v týždni
def week_day(final_date):
    if final_date == 0 or final_date == 7:
        return "Pondelok"
    elif final_date == 1 or final_date == 8:
        return "Utorok"
    elif final_date == 2:
        return "Streda"
    elif final_date == 3:
        return "Štvrtok"
    elif final_date == 4:
        return "Piatok"
    elif final_date == 5:
        return "Sobota"
    elif final_date == 6:
        return "Nedeľa"

# Určenie služby podľa zadaného dátumu
def shift(create_date):
    if my_next_shift in date_list:
        return ("\nDňa %s, %s, máš dennú."%(my_next_shift,week_day(day_shift)))
    elif my_next_shift-datetime.timedelta(days=1) in date_list:
        return ("\n%s, %s, maš nočnú."%(my_next_shift,week_day(day_shift)))
    elif my_next_shift-datetime.timedelta(days=2) in date_list:
        return ("\n%s, %s, budeš po nočnej."%(my_next_shift,week_day(day_shift)))
    elif my_next_shift-datetime.timedelta(days=3) in date_list:
        return ("\n%s, %s, máš 1. volný deň."%(my_next_shift,week_day(day_shift)))
    elif my_next_shift-datetime.timedelta(days=4) in date_list:
        return ("%s, %s, máš 2. volný deň."%(my_next_shift,week_day(day_shift)))
    else:
        return "NEZNÁMA CHYBA!"

# Základné premenné
date_today = datetime.datetime.now()
year_today = date_today.year
month_today = date_today.month
next_shift = int(input("Koľkého máš nasledujúcu službu: "))
next_year_today = year_today + 1
create_date = datetime.date(year_today, month_today, next_shift)
date_list=[]
input_year = int(input("Zadaj rok: "))
input_month = int(input("Zadaj mesiac: "))
input_day = int(input("Zadaj deň: "))
my_next_shift = datetime.date(input_year, input_month, input_day)
day_shift = calendar.weekday(input_year,input_month,input_day)
year_today_count = int(365 / 5)

# Úprava premennej month_today a date podľa výsledku funkcie correct_month(input_day)
create_date = datetime.date(year_today, correct_month(input_day), next_shift)

# Vytvorenie zoznamu všetkých dátumov
date_list=[create_date + datetime.timedelta(days=5)]

for x in range(year_today_count):
    create_date += datetime.timedelta(days=5)
    date_list.append(create_date)

print(shift(create_date))

# Pokračovať vo výpise služieb
print("Praješ si ukázať zoznam všetkých denných?\n")
answer_dates = input("Zadaj A pre áno, alebo N pre nie: ")
print()

# Výpis služieb do marca budúceho roku s dátumom, dňom a typom služby
create_date = datetime.date(year_today, month_today, next_shift)
if answer_dates == "a" or answer_dates == "A":
    for i in range(year_today_count):
        while create_date < datetime.date(next_year_today, 3, 1):
            create_date += datetime.timedelta(days=5)
            print_date_year = int(create_date.strftime("%Y"))
            print_date_month = int(create_date.strftime("%m"))
            print_date_day = int(create_date.strftime("%d"))

            final_date = calendar.weekday(print_date_year,print_date_month,print_date_day)
            print(create_date, end= ", {}, máš dennú\n".format(week_day(final_date)))
            print(create_date+datetime.timedelta(days=1), 
                  end= ", {}, si pred nočnou\n".format(week_day(final_date+1)))
            print(create_date+datetime.timedelta(days=2), end= ", {}, si po nočnej\n".format(week_day(final_date+2)))
            print()

# Konečná komunikácia
    print("Toto sú všetky služby do marca nasledujúceho roku. Ďakujem, dovidenia.")
elif answer_dates == "n" or answer_dates == "N":
    print("Ďakujem, dovidenia.")
else:
    print("Nesprávna voľba, dovidenia.")
