'''
Problem #2
Same as above.
Input two numbers.
Print which number has less steps to reach 1.
'''
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

steps1, steps2 = 0, 0
    
# Calculate steps for num1
while num1 != 1:
    if num1 % 2 == 0:
        num1 = num1 // 2
    else:
        num1 = 3 * num1 + 1
    steps1 += 1

# Calculate steps for num2
while num2 != 1:
    if num2 % 2 == 0:
        num2 = num2 // 2
    else:
        num2 = 3 * num2 + 1
    steps2 += 1

if steps1 < steps2:
    print(f"{num1} reaches 1 in few steps.")
elif steps2 < steps1:
    print(f"{num2} reaches 1 in few steps.")
else:
    print("Both numbers reach 1 in the same number of steps.")
