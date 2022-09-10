### PERFECT NUMBER ###

# A number is a perfect number if is equal to sum of its proper divisors, that is, 
# sum of its positive divisors excluding the number itself. 
# Write a function to check if a given number is perfect or not. 

# Examples: 

# Input: n = 15
# Output: false
# Divisors of 15 are 1, 3 and 5. Sum of 
# divisors is 9 which is not equal to 15.

# Input: n = 6
# Output: true
# Divisors of 6 are 1, 2 and 3. Sum of 
# divisors is 6.

def isPerfectNumber(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

print("isPerfectNumber: ", isPerfectNumber(6))


### PRIME NUMBER ###

# A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

# Write a function to check if a given number is prime or not.

# Examples:

# Input: n = 11
# Output: true
# There is no number between 1 and 11
# that can divide 11.

# Input: n = 15
# Output: false
# There are numbers between 1 and 15
# that can divide 15.

def isPrimeNumber(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print("isPrimeNumber: ", isPrimeNumber(11))

### PRIME NUMBERS IN RANGE ###

# Write a function to print all prime numbers in a given range.

# Examples:

# Input: low = 5, high = 10
# Output: 5, 7

# Input: low = 10, high = 20
# Output: 11, 13, 17, 19

def primeNumbersInRange(low, high):
    for i in range(low, high):
        if isPrimeNumber(i):
            print(i) 

print("primeNumbersInRange 5, 10: ")
primeNumbersInRange(5, 10)

### PRIME FACTORS ###

# Write a function to print all prime factors of a given number.

# Examples:

# Input: n = 12
# Output: 2, 2, 3

# Input: n = 315
# Output: 3, 3, 5, 7

def primeFactors(n):
    if n <= 1:
        return False
    for i in range (2, n):
        if n % i == 0:
            if isPrimeNumber(i) == True:
                print(i)
print("primeFactors of 12: ")
primeFactors(12)


### FIBONACCI SERIES ###

# Write a function to print first n Fibonacci Numbers.

# Examples:

# Input: n = 7
# Output: 0, 1, 1, 2, 3, 5, 8

# Input: n = 10
# Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

def fibonacciSeries(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)

print("fibonacciSeries of 7: ")
fibonacciSeries(7)

### PALINDROME NUMBER ###

# A palindrome number is a number that is same after reverse.

# Write a function to check if a given number is palindrome or not.

# Examples:

# Input: n = 121
# Output: true

# Input: n = 123
# Output: false

def isPalindromeNumber(n):
    temp = n
    rev = 0
    while temp > 0:
        rev = rev * 10 + temp % 10
        temp = temp // 10
    return rev == n

print("isPalindromeNumber: ", isPalindromeNumber(121))

### PALINDROME STRING ###

# A palindrome string is a string that is same after reverse.

# Write a function to check if a given string is palindrome or not.

# Examples:

# Input: str = "abba"
# Output: true

# Input: str = "abc"
# Output: false

def isPalindromeString(s):
    return s == s[::-1]

print("isPalindromeString: ", isPalindromeString("abba"))

### ARMSTRONG NUMBER ###

# An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself.

# Write a function to check if a given number is Armstrong number or not.

# Examples:

# Input: n = 153
# Output: true

# Input: n = 120
# Output: false

def isArmstrongNumber(n):
    temp = n
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    return sum == n

print("isArmstrongNumber: ", isArmstrongNumber(153))