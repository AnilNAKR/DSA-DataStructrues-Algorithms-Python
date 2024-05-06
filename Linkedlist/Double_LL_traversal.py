class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
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
    # Creation of Double Linked list --> Time complexity is O(1) for DLL and Space is O(1)
    def creationDLL(self, NodeValue):
        node = Node(NodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "The Double Linked list is created Successfully"

    # Insertion of a node in Double Linked List
    def insertDLL(self, Nvalue, location):
        if self.head is None:
            print("The head reference is None and node can't be inserted")
        else:
            newNode = Node(Nvalue)
            if location == 0:
                newNode.next = self.head
                newNode.prev = None
                self.head = newNode
                self.head.prev = newNode
            elif location == 1:
                newNode.prev = self.tail
                newNode.next = None
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
    
    # Traversing Double Linked List
    def traverseDLL(self):
        if self.head is None:
            print("There is not any element to traverse")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
        
DoubleLL = DoubleLinkedList()
DoubleLL.creationDLL(5)
DoubleLL.insertDLL(0,0)
DoubleLL.insertDLL(1,1)
DoubleLL.insertDLL(2,2)
DoubleLL.insertDLL(3,3)
DoubleLL.insertDLL(4,4)
DoubleLL.insertDLL(7,3)


print([node.value for node in DoubleLL])
DoubleLL.traverseDLL()                