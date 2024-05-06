# Creating a Node
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

#Creating Head and a Tail
class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

sLinkedList = SingleLinkedList()
node1 = Node(1) # assigning value to the node
node2 = Node(2)

#Linking head to the 1st node, 1 node to the 2nd node and tail to the last/2nd node
sLinkedList.head = node1
sLinkedList.head.next = node2
sLinkedList.tail = node2

# Step for creating a Single linked List
# 1. Fist create Head and a Tail with Null references
# 2. Then create a empty node with NULL reference
# 3. Then assign the value to the empty node and connect Head reference to 1st node
# 1st node reference to 2nd node, and Tail to the last node  