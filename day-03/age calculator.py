from datetime import date

# capture a name
name = input("Please enter your name: ")
year_born = input("Please enter the year you were born: ")

today = date.today()

age = today.year - int(year_born)

print(name, " is ", age) 