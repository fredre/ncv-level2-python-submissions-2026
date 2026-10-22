name = ""
staffnum = ""
level = ""

while not name:
    name = input("Name: ")
    if not name:
        print("Please enter name and do not just press enter")
        
while not staffnum.isdigit():
    staffnum = input("Staff number: ")
    if not staffnum.isdigit():
        print("Enter numbers only")
    

while not level.isdigit():
    level = input("Level: ")
    if not level.isdigit():
        print("Enter numbers only")
        
print(name, " ", staffnum, " ", level)