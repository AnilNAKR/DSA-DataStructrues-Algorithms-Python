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

CDLL = CircularDLL()
print(CDLL.createCDLL(1))
print([node.value for node in CDLL])



        