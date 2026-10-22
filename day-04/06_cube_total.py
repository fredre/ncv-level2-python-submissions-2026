number = int(input("number: "))
loopy = number+1
total = int(0)
for power in range(1,number+1):
    print(power ** 3, end=",")
    total = total + (power ** 3)
print("total: ", total)