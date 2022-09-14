### How do you print duplicate characters from a string? ###

# 1. use hash table to store the characters
# 2. for each character, check if the character is present in the hash table
# 3. if the character is present, print the character
# 4. if the character is not present, add the character to the hash table
def printDuplicates(str):
    hashTable = {}
    for i in str:
        if i in hashTable:
            print("Duplicate: ", i)
        else:
            hashTable[i] = i

# 5. Resultant will be the duplicates
if __name__ == "__main__":
    str = "Hello World"
    printDuplicates(str)

# 6. Time complexity is O(n)

### How do you check if two strings are anagrams of each other? ###

# anagram: a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.

# 1. use hash table to store the characters
# 2. for each character, check if the character is present in the hash table
# 3. if the character is present, increment the count
# 4. if the character is not present, add the character to the hash table
def checkAnagram(str1, str2):
    hashTable = {}
    for i in str1:
        if i in hashTable:
            hashTable[i] += 1
        else:
            hashTable[i] = 1
    for j in str2:
        if j in hashTable:
            hashTable[j] -= 1
        else:
            hashTable[j] = 1
    for k in hashTable:
        if hashTable[k] != 0:
            return False
    return True

# 5. Resultant will be the duplicates
if __name__ == "__main__":
    str1 = "cinema"
    str2 = "iceman"
    print(checkAnagram(str1, str2))

# 6. Time complexity is O(n)

### How do you print the first non-repeated character from a string? ###

# 1. use hash table to store the characters
# 2. for each character, check if the character is present in the hash table
# 3. if the character is present, increment the count
# 4. if the character is not present, add the character to the hash table
def printFirstNonRepeated(str):
    hashTable = {}
    for i in str:
        if i in hashTable:
            hashTable[i] += 1
        else:
            hashTable[i] = 1
    for j in str:
        if hashTable[j] == 1:
            return j
    return None

# 5. Resultant will be the duplicates
if __name__ == "__main__":
    str = "Hello World"
    print(printFirstNonRepeated(str))

# 6. Time complexity is O(n)

### How do you find all permutations of a string? ###

# 1. use hash table to store the characters
# 2. for each character, check if the character is present in the hash table
# 3. if the character is present, increment the count
# 4. if the character is not present, add the character to the hash table
def printPermutations(str):
    hashTable = {}
    for i in str:
        if i in hashTable:
            hashTable[i] += 1
        else:
            hashTable[i] = 1
    print(hashTable)

# 5. Resultant will be the duplicates
if __name__ == "__main__":
    str = "Hello World"
    printPermutations(str)

# 6. Time complexity is O(n)

### How do you reverse words in a given sentence without using any library method? ###

def reverseWords(str):
    str = str.split(" ")
    str = str[::-1]
    str = " ".join(str)
    return str

# 5. Resultant will be the duplicates
if __name__ == "__main__":
    str = "Hello World"
    print(reverseWords(str))

# 6. Time complexity is O(n)

### How do you check if a given string is a palindrome? ###

def checkPalindrome(str):
    str = str.lower()
    str = str.replace(" ", "")
    return str == str[::-1]

# 5. Resultant will be the duplicates
if __name__ == "__main__":
    str = "Hello World"
    print(checkPalindrome(str))

# 6. Time complexity is O(n)

### How do you check if a given string is a rotation of a palindrome? ###

def checkRotationPalindrome(str):
    str = str.lower()
    str = str.replace(" ", "")
    str = str + str

    print(str)
    print(str[::-1])
    return str == str[::-1]

# 5. Resultant will be the duplicates
if __name__ == "__main__":
    str = "1214"
    print(checkRotationPalindrome(str))

# 6. Time complexity is O(n)

### How do you check if a string contains only digits? ###

def checkDigits(str):
    for i in str:
        if i.isdigit() == False:
            return False
    return True

# 5. Resultant will be the duplicates
if __name__ == "__main__":
    str = "Hello World"
    print(checkDigits(str))

# 6. Time complexity is O(n)

### How do you count a number of vowels and consonants in a given string? ###

def countVowelsConsonants(str):
    vowels = "aeiou"
    vowelsCount = 0
    consonantsCount = 0
    for i in str:
        if i in vowels:
            vowelsCount += 1
        else:
            consonantsCount += 1
    print("Vowels: ", vowelsCount)
    print("Consonants: ", consonantsCount)

# 5. Resultant will be the duplicates
if __name__ == "__main__":
    str = "Hello World"
    countVowelsConsonants(str)

# 6. Time complexity is O(n)

### How do you count the occurrence of a given character in a string? ###

def countOccurrence(str, char):
    count = 0
    for i in str:
        if i == char:
            count += 1
    return count

# 5. Resultant will be the duplicates
if __name__ == "__main__":
    str = "Hello World"
    char = "l"
    print(countOccurrence(str, char))

# 6. Time complexity is O(n)

