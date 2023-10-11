'''
Problem #1
Write a program for Collatz_conjecture.
Collatz_conjecture means -  start with the input number. 
For even number , divide by 2 (n/2)
For odd number - 3n + 1
apply the above for the result number until the answer is 1.

'''
n = int(input("Enter a number: "))

while n != 1:
    print(n, end=' ')
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1

print(1)
