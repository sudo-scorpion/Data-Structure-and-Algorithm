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

print(isPerfectNumber(6))


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