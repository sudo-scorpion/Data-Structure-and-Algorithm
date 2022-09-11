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


### ARMSTRONG NUMBER IN RANGE ###

# Write a function to print all Armstrong numbers in a given range.

# Examples:

# Input: low = 100, high = 500
# Output: 153, 370, 371, 407

# Input: low = 1000, high = 5000
# Output: 1534, 3704, 3714, 4074

def armstrongNumbersInRange(low, high):
    for i in range(low, high):
        if isArmstrongNumber(i):
            print(i)

print("armstrongNumbersInRange 100, 500: ")
armstrongNumbersInRange(100, 500)

### BUBBLE SORT ###

# Bubble sort is a simple sorting algorithm that repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order.

# Write a function to sort a given list using bubble sort.

# Examples:

# Input: arr = [64, 34, 25, 12, 22, 11, 90]
# Output: [11, 12, 22, 25, 34, 64, 90]

# Input: arr = [64, 34, 25, 12, 22, 11, 90, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 22, 25, 34, 64, 90]

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print("bubbleSort: ", bubbleSort([64, 34, 25, 12, 22, 11, 90]))

### SELECTION SORT ###

# Selection sort is a simple sorting algorithm. This sorting algorithm is an in-place comparison-based algorithm in which the list is divided into two parts, the sorted part at the left end and the unsorted part at the right end.

# Write a function to sort a given list using selection sort.

# Examples:

# Input: arr = [64, 25, 12, 22, 11]
# Output: [11, 12, 22, 25, 64]

# Input: arr = [64, 34, 25, 12, 22, 11, 90, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 22, 25, 34, 64, 90]

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print("selectionSort: ", selectionSort([64, 25, 12, 22, 11]))

### INSERTION SORT ###

# Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.

# Write a function to sort a given list using insertion sort.

# Examples:

# Input: arr = [12, 11, 13, 5, 6]
# Output: [5, 6, 11, 12, 13]

# Input: arr = [64, 34, 25, 12, 22, 11, 90, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 22, 25, 34, 64, 90]

def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print("insertionSort: ", insertionSort([12, 11, 13, 5, 6]))

### MERGE SORT ###

# Merge sort is a divide and conquer algorithm. It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves.

# Write a function to sort a given list using merge sort.

# Examples:

# Input: arr = [12, 11, 13, 5, 6, 7]
# Output: [5, 6, 7, 11, 12, 13]

# Input: arr = [64, 34, 25, 12, 22, 11, 90, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 22, 25, 34, 64, 90]

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

print("mergeSort: ", mergeSort([12, 11, 13, 5, 6, 7]))

### QUICK SORT ###

# Quick sort is a divide and conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot.

# Write a function to sort a given list using quick sort.

# Examples:

# Input: arr = [10, 7, 8, 9, 1, 5]
# Output: [1, 5, 7, 8, 9, 10]

# Input: arr = [64, 34, 25, 12, 22, 11, 90, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 22, 25, 34, 64, 90]

def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
    return arr

print("quickSort: ", quickSort([10, 7, 8, 9, 1, 5], 0, 5))

### HEAP SORT ###

# Heap sort is a comparison based sorting technique based on Binary Heap data structure. It is similar to selection sort where we first find the maximum element and place the maximum element at the end. We repeat the same process for remaining element.

# Write a function to sort a given list using heap sort.

# Examples:

# Input: arr = [12, 11, 13, 5, 6, 7]
# Output: [5, 6, 7, 11, 12, 13]

# Input: arr = [64, 34, 25, 12, 22, 11, 90, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 22, 25, 34, 64, 90]

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

print("heapSort: ", heapSort([12, 11, 13, 5, 6, 7]))

### BINARY SEARCH ###

# Binary search is a search algorithm that finds the position of a target value within a sorted array.

# Write a function to search a given list using binary search.

# Examples:

# Input: arr = [2, 3, 4, 10, 40], x = 10
# Output: 3

# Input: arr = [2, 3, 4, 10, 40], x = 50
# Output: -1

def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1

print("binarySearch: ", binarySearch([2, 3, 4, 10, 40], 0, 4, 10))


### BINARY SEARCH TREE ###
# Binary search tree is a node-based binary tree data structure which has the following properties:

# The left subtree of a node contains only nodes with keys lesser than the node’s key.

# The right subtree of a node contains only nodes with keys greater than the node’s key.

# The left and right subtree each must also be a binary search tree.

# There must be no duplicate nodes.

# Write a function to search a given list using binary search tree.

# Examples:

# Input: arr = [2, 3, 4, 10, 40], x = 10
# Output: 3

# Input: arr = [2, 3, 4, 10, 40], x = 50
# Output: -1

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)

r = Node(50)
insert(r, Node(30))
insert(r, Node(20))
insert(r, Node(40))
insert(r, Node(70))
insert(r, Node(60))
insert(r, Node(80))

print("binarySearchTree: ", search(r, 80))



### LINKED LIST ###

# Linked list is a linear data structure, in which the elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers.

# Write a function to search a given list using linked list.

# Examples:

# Input: arr = [2, 3, 4, 10, 40], x = 10

# Output: 3

# Input: arr = [2, 3, 4, 10, 40], x = 50

# Output: -1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def search(self, x):
        current = self.head
        while current != None:
            if current.data == x:
                return True
            current = current.next
        return False

llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)
llist.head.next = second
second.next = third

print("linked list: ", llist.search(3))


### GRAPH ###

# Graph is a non-linear data structure consisting of nodes and edges. The nodes are sometimes also referred to as vertices and the edges are lines or arcs that connect any two nodes in the graph.

# Write a function to search a given list using graph.

# Examples:

# Input: arr = [2, 3, 4, 10, 40], x = 10

# Output: 3

# Input: arr = [2, 3, 4, 10, 40], x = 50

# Output: -1

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def isSafe(self, v, pos, path):
        if self.graph[path[pos - 1]][v] == 0:
            return False
        for vertex in path:
            if vertex == v:
                return False
        return True

    def hamCycleUtil(self, path, pos):
        if pos == self.V:
            if self.graph[path[pos - 1]][path[0]] == 1:
                return True
            else:
                return False
        for v in range(1, self.V):
            if self.isSafe(v, pos, path) == True:
                path[pos] = v
                if self.hamCycleUtil(path, pos + 1) == True:
                    return True
                path[pos] = -1
        return False

    def hamCycle(self):
        path = [-1] * self.V
        path[0] = 0
        if self.hamCycleUtil(path, 1) == False:
            print("Solution does not exist")
            return False
        self.printSolution(path)
        return True

    def printSolution(self, path):
        print("Solution Exists: Following is one Hamiltonian Cycle")
        for vertex in path:
            print(vertex, end=" ")
        print(path[0], "\n")

g1 = Graph(5)
g1.graph = [[0, 1, 0, 1, 0], [1, 0, 1, 1, 1], [0, 1, 0, 0, 1], [1, 1, 0, 0, 1], [0, 1, 1, 1, 0]]    
g1.hamCycle()

g2 = Graph(5)
g2.graph = [[0, 1, 0, 1, 0], [1, 0, 1, 1, 1], [0, 1, 0, 0, 1], [1, 1, 0, 0, 0], [0, 1, 1, 0, 0]]
g2.hamCycle()


### HASH TABLE ###
# Hash table is a data structure which is used to implement an associative array, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.

# Write a function to search a given list using hash table.

# Examples:

# Input: arr = [2, 3, 4, 10, 40], x = 10

# Output: 3

# Input: arr = [2, 3, 4, 10, 40], x = 50

# Output: -1

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __getitem__(self, index):
        h = self.get_hash(index)
        for element in self.arr[h]:
            if element[0] == index:
                return element[1]

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for index, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]

t = HashTable()
t["march 6"] = 310
t["march 7"] = 420
t["march 8"] = 280
t["march 9"] = 390
t["march 17"] = 120
print(t.arr)
print(t["march 6"])
del t["march 6"]
print(t.arr)


### HEAP ###

# Heap is a specialized tree-based data structure that satisfies the heap property: if P is a parent node of C, then the key (the value) of P is either greater than or equal to (in a max heap) or less than or equal to (in a min heap) the key of C.

# Write a function to search a given list using heap.

# Examples:

# Input: arr = [2, 3, 4, 10, 40], x = 10

# Output: 3

# Input: arr = [2, 3, 4, 10, 40], x = 50

# Output: -1

class Heap:
    def __init__(self, arr):
        self.heap = arr
        self.size = len(arr)
        self.build_max_heap()

    def build_max_heap(self):
        for i in range(self.size // 2, -1, -1):
            self.max_heapify(i)

    def max_heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < self.size and self.heap[left] > self.heap[largest]:
            largest = left
        if right < self.size and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)

    def extract_max(self):
        max = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.max_heapify(0)
        return max

    def search(self, x):
        for i in range(self.size):
            if self.heap[i] == x:
                return i
        return -1

arr = [2, 3, 4, 10, 40]
heap = Heap(arr)
print(heap.search(10))
print(heap.search(50))



