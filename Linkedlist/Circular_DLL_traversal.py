class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

class CircularDLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
# Creation of Circular Double Linked list            
    def createCDLL(self, Nvalue):
        newNode = Node(Nvalue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = self.head
        newNode.next = newNode
        return "The Circular Double Linked list is created successfully"

# Insert a node in CDLL
    def insertCDLL(self, value, location):
        if self.head is None:
            return "The CDLL does not exist"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head = newNode
                self.head.prev = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                tempNode.next = newNode
                newNode.next.prev = newNode
            return "The node has been successfully inserted"

# CDLL Traversal
    def traversalCDLL(self):
        if self.head is None:
            print("There are no elements in the list")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next


CDLL = CircularDLL()
print(CDLL.createCDLL(1))
CDLL.insertCDLL(0,0)
CDLL.insertCDLL(1,1)
CDLL.insertCDLL(2,2)
CDLL.insertCDLL(3,3)
CDLL.insertCDLL(4,4)
print([node.value for node in CDLL])
CDLL.traversalCDLL()




        