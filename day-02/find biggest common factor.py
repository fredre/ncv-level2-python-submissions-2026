# this program will only calculate the biggest common factor
# for numbers that have a common factor! 

# Prompt user for inputs
a = int(input("Enter the first integer Biggest: "))
b = int(input("Enter the second integer Smallest: "))

# test
while b != 0:
    r = a % b  #(modulo)
    a = b
    b = r
  
#display result  
print(a)