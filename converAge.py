from datetime import date
# ask the user date of birth

# year
yearOfBirth = input("Enter your year of birth\n")
while not (yearOfBirth.isnumeric() and int(yearOfBirth) in range(1, 2024)):
    yearOfBirth = input("Wrong number. Enter your year of birth\n")
yearOfBirth = int(yearOfBirth)

# month
monthOfBirth = input("Enter your month of birth\n")
while not (monthOfBirth.isdigit() and int(monthOfBirth) in range(1, 13)):
    monthOfBirth = input("Wrong number. Enter your month of birth\n")
monthOfBirth = int(monthOfBirth)

# day
dayOfBirth = input("Enter your day of birth\n")
while not dayOfBirth.isnumeric():
    dayOfBirth = input("Wrong number. Enter your day of birth\n")
    if monthOfBirth in [4, 6, 9, 11]:
        while int(dayOfBirth) not in range(1, 31):
            dayOfBirth = input("Your month does not have such date in it. Enter your day of birth\n")
    if monthOfBirth in [1, 3, 5, 7, 8, 10, 12]:
        while int(dayOfBirth) not in range(1, 32):
            dayOfBirth = input("Your month does not have such date in it. Enter your day of birth\n")
    if monthOfBirth in [2]:
        if (yearOfBirth % 4) == 0:
            while int(dayOfBirth) not in range(1, 30):
                dayOfBirth = input("Your month does not have such date in it. Enter your day of birth\n")
        else:
            while int(dayOfBirth) not in range(1, 29):
                dayOfBirth = input("Your month does not have such date in it. Enter your day of birth\n")
dayOfBirth = int(dayOfBirth)

# today and birthdate
now = date.today()
birth = date(year=yearOfBirth, month=monthOfBirth, day=dayOfBirth)
today = date(year=int(now.year), month=int(now.month), day=int(now.day))

# calculate age
age = today - birth

# count their age in days, hours and minutes
ageDays = age.days
seconds = age.total_seconds()
minutes = int(seconds) / 60
hours = int(minutes) / 60

# output
print(f'You have lived for {ageDays} days or {int(hours)} hours or {int(minutes)} minutes or {int(seconds)} seconds. But actually, while reading it, you have lived for 15 seconds more)')
