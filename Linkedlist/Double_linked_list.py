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

DoubleLL = DoubleLinkedList()
DoubleLL.creationDLL(5)

print([node.value for node in DoubleLL])
                