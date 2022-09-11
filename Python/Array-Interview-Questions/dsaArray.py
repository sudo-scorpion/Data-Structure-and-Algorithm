### How do you find the missing number in a given integer array of 1 to 100? ###

# 1. Find the sum of all numbers from 1 to 100
def sumOfNumbers(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

# 2. Subtract all the numbers in the array from sum of first n natural numbers
def missingNumber(arr, n):
    sum = sumOfNumbers(n)
    for i in arr:
        sum -= i
    return sum

# 3. Resultant will be the missing number
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 6, 7, 8, 9, 10]
    n = len(arr) + 1
    print("Missing number is", missingNumber(arr, n))

# 4. Time complexity is O(n)

### How do you find the duplicate number on a given integer array? ###

# 1. Sort the array
def sortArray(arr):
    arr.sort()
    return arr

# 2. Compare each element with the next element
def duplicateNumber(arr):
    arr = sortArray(arr)
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            return arr[i]

# 3. Resultant will be the duplicate number
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 2, 7, 8, 9, 10]
    print("Duplicate number is", duplicateNumber(arr))

# 4. Time complexity is O(nlogn)


### How do you find the largest and smallest number in an unsorted integer array? ###

# 1. Sort the array
def sortArray(arr):
    arr.sort()
    return arr

# 2. Largest number will be the last element
# 3. Smallest number will be the first element
def largestAndSmallest(arr):
    arr = sortArray(arr)
    return arr[0], arr[-1]

# 4. Resultant will be the largest and smallest number
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 2, 7, 8, 9, 10]
    smallest, largest = largestAndSmallest(arr)
    print("Smallest number is", smallest)
    print("Largest number is", largest)

# 5. Time complexity is O(nlogn)


### How do you find all pairs of an integer array whose sum is equal to a given number? ###

# 1. use hash table to store the numbers
# 2. for each number, check if the number is present in the hash table
# 3. if the number is present, print the pair
# 4. if the number is not present, add the number to the hash table
def findPairs(arr, n):
    hashTable = {}
    for i in arr:
        if i in hashTable:
            print(i, n-i)
        else:
            hashTable[n-i] = i

# 5. Resultant will be the pairs
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 2, 7, 8, 9, 10]
    n = 10
    findPairs(arr, n)

# 6. Time complexity is O(n)

### How do you find duplicate numbers in an array if it contains multiple duplicates? ###

# 1. use hash table to store the numbers
# 2. for each number, check if the number is present in the hash table
# 3. if the number is present, print the number
# 4. if the number is not present, add the number to the hash table
def findDuplicates(arr):
    hashTable = {}
    for i in arr:
        if i in hashTable:
            print("Multiple duplicates: ", i)
        else:
            hashTable[i] = i

# 5. Resultant will be the duplicates
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 2, 7, 7, 8, 9, 10]
    findDuplicates(arr)


### How are duplicates removed from a given array? ###

# 1. use hash table to store the numbers
# 2. for each number, check if the number is present in the hash table
# 3. if the number is present, do nothing
# 4. if the number is not present, add the number to the hash table
def removeDuplicates(arr):
    hashTable = {}
    for i in arr:
        if i in hashTable:
            continue
        else:
            hashTable[i] = i
    return hashTable

# 5. Resultant will be the array without duplicates
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 2, 7, 7, 8, 9, 10]
    print("Array without duplicates:", removeDuplicates(arr))

# 6. Time complexity is O(n)


### How is an integer array sorted in place using the quicksort algorithm? ###

# 1. use the first element as pivot
# 2. use two pointers, one at the beginning and one at the end
# 3. move the left pointer until you find an element greater than the pivot
# 4. move the right pointer until you find an element less than the pivot
# 5. swap the elements at the left and right pointers
# 6. repeat step 3 and 4 until the left pointer is greater than the right pointer
# 7. swap the pivot with the element at the right pointer
# 8. repeat step 1 to 7 for the left and right subarrays
def quickSort(arr, left, right):
    if left < right:
        pivot = arr[left]
        i = left
        j = right
        while i < j:
            while i < len(arr) and arr[i] <= pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[left], arr[j] = arr[j], arr[left]
        quickSort(arr, left, j-1)
        quickSort(arr, j+1, right)

# 9. Resultant will be the sorted array
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 2, 7, 7, 8, 9, 10]
    quickSort(arr, 0, len(arr)-1)
    print("Sorted array:", arr)

# 10. Time complexity is O(nlogn)


### How do you remove duplicates from an array in place? ###

# remove duplicates from an array in place
def removeDuplicates(arr):
    if len(arr) == 0:
        return 0
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    return arr[:i+1]

# resultant will be the array without duplicates
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 2, 7, 7, 7, 8, 9, 10]
    print("Array without duplicates:", removeDuplicates(arr))

# time complexity is O(n)

### How do you reverse an array in place? ###

# 1. use two pointers, one at the beginning and one at the end
# 2. swap the elements at the left and right pointers
# 3. move the left pointer to the right and the right pointer to the left
# 4. repeat step 2 and 3 until the left pointer is greater than the right pointer
def reverseArray(arr):
    left = 0
    right = len(arr)-1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

# 5. Resultant will be the reversed array
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 7, 7, 8, 9, 10]
    reverseArray(arr)
    print("Reversed array:", arr)

