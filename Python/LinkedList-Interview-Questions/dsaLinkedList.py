### How do you find the middle element of a singly linked list in one pass? ###

# 1. use two pointers, one at the beginning and one at the end
# 2. move the left pointer to the next node
# 3. move the right pointer to the next node and then to the next node
# 4. repeat step 2 and 3 until the right pointer is null
# 5. the node at the left pointer is the middle element
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def middleElement(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

if __name__ == "__main__":
    llist = LinkedList()
    for i in range(1, 11):
        llist.push(i)
    llist.printList()
    print("Middle element:", llist.middleElement())

# time complexity is O(n)

### How do you check if a given linked list contains a cycle? ###

# 1. use two pointers, one at the beginning and one at the end
# 2. move the left pointer to the next node 
# 3. move the right pointer to the next node and then to the next node
# 4. repeat step 2 and 3 until the right pointer is null
# 5. if the left pointer is equal to the right pointer, then the linked list contains a cycle
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

if __name__ == "__main__":
    llist = LinkedList()
    for i in range(1, 11):
        llist.push(i)
    llist.printList()
    print("Does the linked list contain a cycle?", llist.cycle())

# time complexity is O(n)

### How do you reverse a linked list? ###

# 1. use three pointers, one at the beginning, one at the middle and one at the end
# 2. move the middle pointer to the next node
# 3. move the end pointer to the next node and then to the next node
# 4. repeat step 2 and 3 until the end pointer is null
# 5. set the next pointer of the middle pointer to the beginning pointer
# 6. set the beginning pointer to the middle pointer
# 7. set the middle pointer to the end pointer
# 8. repeat step 5, 6 and 7 until the middle pointer is null
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

if __name__ == "__main__":
    llist = LinkedList()
    for i in range(1, 11):
        llist.push(i)
    llist.printList()
    llist.reverse()
    llist.printList()

# time complexity is O(n)

### How do you find the third node from the end in a singly linked list? ###
# 1. use three pointers, one at the beginning, one at the middle and one at the end
# 2. move the middle pointer to the next node
# 3. move the end pointer to the next node and then to the next node
# 4. repeat step 2 and 3 until the end pointer is null
# 5. set the beginning pointer to the middle pointer
# 6. set the middle pointer to the end pointer
# 7. repeat step 5 and 6 until the middle pointer is null
# 8. return the data of the beginning pointer
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def thirdNode(self):
        first = self.head
        second = self.head
        third = self.head
        while third and third.next:
            first = second
            second = third
            third = third.next
        return first.data

if __name__ == "__main__":
    llist = LinkedList()
    for i in range(1, 11):
        llist.push(i)
    llist.printList()
    print("Third node from the end:", llist.thirdNode())

# time complexity is O(n)

### How do you find the sum of two linked lists using Stack? ###

# 1. use two stacks
# 2. push the elements of the first linked list to the first stack
# 3. push the elements of the second linked list to the second stack
# 4. pop the elements from the first stack and add them to the sum
# 5. pop the elements from the second stack and add them to the sum
# 6. return the sum
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def sum(self, llist):
        stack1 = []
        stack2 = []
        temp = self.head
        while temp:
            stack1.append(temp.data)
            temp = temp.next
        temp = llist.head
        while temp:
            stack2.append(temp.data)
            temp = temp.next
        sum = 0
        while stack1:
            sum += stack1.pop()
        while stack2:
            sum += stack2.pop()
        return sum

if __name__ == "__main__":
    llist = LinkedList()
    for i in range(1, 11):
        llist.push(i)
    llist.printList()
    llist2 = LinkedList()
    for i in range(11, 21):
        llist2.push(i)
    llist2.printList()
    print("Sum of two linked lists:", llist.sum(llist2))

# time complexity is O(n)

### How do you find the middle element of a linked list? ###

# 1. use two pointers, one at the beginning and one at the end
# 2. move the beginning pointer to the next node
# 3. move the end pointer to the next node and then to the next node
# 4. repeat step 2 and 3 until the end pointer is null
# 5. return the data of the beginning pointer
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

if __name__ == "__main__":
    llist = LinkedList()
    for i in range(1, 11):
        llist.push(i)
    llist.printList()
    print("Middle element:", llist.middle())

# time complexity is O(n)


### How do you check if a given linked list contains a cycle? ###

# 1. use two pointers, one at the beginning and one at the end
# 2. move the beginning pointer to the next node
# 3. move the end pointer to the next node and then to the next node
# 4. repeat step 2 and 3 until the end pointer is null
# 5. if the beginning pointer is equal to the end pointer, return true
# 6. return false
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

if __name__ == "__main__":
    llist = LinkedList()
    for i in range(1, 11):
        llist.push(i)
    llist.printList()
    print("Cycle:", llist.cycle())

# time complexity is O(n)

### How do you reverse a linked list? ###
# 1. use three pointers, one at the beginning, one at the middle and one at the end
# 2. set the middle pointer to the beginning pointer
# 3. set the beginning pointer to the end pointer
# 4. set the end pointer to the next node of the middle pointer
# 5. repeat step 2, 3 and 4 until the end pointer is null
# 6. set the head to the beginning pointer
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

if __name__ == "__main__":
    llist = LinkedList()
    for i in range(1, 11):
        llist.push(i)
    llist.printList()
    llist.reverse()
    llist.printList()

# time complexity is O(n)

### How do you reverse a linked list in groups of given size? ###
# 1. use three pointers, one at the beginning, one at the middle and one at the end
# 2. set the middle pointer to the beginning pointer
# 3. set the beginning pointer to the end pointer
# 4. set the end pointer to the next node of the middle pointer
# 5. repeat step 2, 3 and 4 until the end pointer is null
# 6. set the head to the beginning pointer
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def reverse(self, k):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

if __name__ == "__main__":
    llist = LinkedList()
    for i in range(1, 11):
        llist.push(i)
    llist.printList()
    llist.reverse(3)
    llist.printList()

# time complexity is O(n)

### How do you find the third node from the end in a linked list? ###

# 1. use three pointers, one at the beginning, one at the middle and one at the end
# 2. move the beginning pointer to the next node
# 3. move the middle pointer to the next node
# 4. move the end pointer to the next node and then to the next node
# 5. repeat step 2, 3 and 4 until the end pointer is null
# 6. return the data of the middle pointer
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def third(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

if __name__ == "__main__":
    llist = LinkedList()
    for i in range(1, 11):
        llist.push(i)
    llist.printList()
    print("Third element:", llist.third())

# time complexity is O(n)

### How do you find the sum of two linked lists using Stack? ###
# 1. use two stacks
# 2. push the first linked list to the first stack
# 3. push the second linked list to the second stack
# 4. create a new linked list
# 5. create a variable to store the carry
# 6. while the first stack is not empty or the second stack is not empty
# 7. create a variable to store the sum
# 8. if the first stack is not empty, add the top of the first stack to the sum
# 9. if the second stack is not empty, add the top of the second stack to the sum
# 10. add the carry to the sum
# 11. create a new node with the sum modulo 10
# 12. set the carry to the sum divided by 10
# 13. push the new node to the new linked list
# 14. return the new linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def sum(self, llist):
        stack1 = []
        stack2 = []
        temp = self.head
        while temp:
            stack1.append(temp.data)
            temp = temp.next
        temp = llist.head
        while temp:
            stack2.append(temp.data)
            temp = temp.next
        llist = LinkedList()
        carry = 0
        while stack1 or stack2:
            sum = carry
            if stack1:
                sum += stack1.pop()
            if stack2:
                sum += stack2.pop()
            newNode = Node(sum % 10)
            carry = sum // 10
            newNode.next = llist.head
            llist.head = newNode
        return llist

if __name__ == "__main__":
    llist1 = LinkedList()
    llist2 = LinkedList()
    for i in range(1, 11):
        llist1.push(i)
        llist2.push(i)
    llist1.printList()
    llist2.printList()
    llist3 = llist1.sum(llist2)
    llist3.printList()

# time complexity is O(n)
