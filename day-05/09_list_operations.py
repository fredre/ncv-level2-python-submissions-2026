marks = []
mark = int(input("enter mark "))
total = 0
total = total + mark

while mark != -1:
    marks.append(mark)
    mark = int(input("enter mark "))
    total = total + mark
    
print (f"our list has {len(marks)} elements")

for i in range(len(marks)):
    print(marks[i])
    
avg = total / len(marks)
print(f"Average: {avg}")