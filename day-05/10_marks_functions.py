def getmarks():
    marks = []
    mark = int(input("enter mark "))
    while mark != -1:
        marks.append(mark)
        mark = int(input("enter mark "))
    return marks

def print_list_size(marks):
    print (f"our list has {len(marks)} elements")
    
def print_marks(marks):
    for i in range(len(marks)):
        print(marks[i])

def get_sum_marks(marks):
    total = 0
    for i in range(len(marks)):
        mark = marks[i]
        total = total + mark
    return total

def calc_ave(total):
    avg = total / len(marks)
    print(f"Average: {avg}")
    return avg

def highest(marks):
    highest = 0
    for i in range(len(marks)):
        current_mark = marks[i]
        if current_mark > highest:
            highest = current_mark
    print(f"the highest is {highest}")
    
menu = "press 1: mark capture\n"
menu += "press 2: number of marks\n"
menu += "press 3: avarage of marks\n"
menu += "press 4: highest mark\n"
menu += "press 1-: exit\n"



working_marks = []
choice = 0

while choice != -1:
    print(menu)
    choice = int(input("choice : "))
    
    if choice == 1:
        working_marks = getmarks()
        
    elif choice == 2:
        print_list_size(working_marks)
        
    elif choice == 3:
        calc_ave(working_marks)
        
    elif choice == 4:
        highest(working_marks)
        
print("ok baai!")
