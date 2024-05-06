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
        newNode.prev = newNode
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
                self.head.prev = newNode
                self.head = newNode
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
                newNode.next.prev = newNode
                tempNode.next = newNode     
            return "The node has been successfully inserted"

# # CDLL Traversal
#     def traversalCDLL(self):
#         if self.head is None:
#             print("There are no elements in the list")
#         else:
#             tempNode = self.head
#             while tempNode:
#                 print(tempNode.value)
#                 if tempNode == self.tail:
#                     break
#                 tempNode = tempNode.next

# # Reverese Traversal
#     def reverseTraversalCDLL(self):
#             if self.head is None:
#                 print("There is not any node for reverse traversal")
#             else:
#                 tempNode = self.tail
#                 while tempNode:
#                     print(tempNode.value)
#                     if tempNode == self.head:
#                         break
#                     tempNode = tempNode.prev
        
# # Searching for a node value in the list
#     def searchCDLL(self, Nvalue):
#         if self.head is None:
#             print("There are no elements in the list")
#         else:
#             tempNode = self.head
#             while tempNode:
#                 if tempNode.value == Nvalue:
#                     return tempNode.value
#                 if tempNode == self.tail:
#                     return "The value does not exist in CDLL"
#                 tempNode = tempNode.next

# # Delete a node from a CDLL
#     def deleteNodeCDLL(self, location):
#         if self.head is None:
#             print("There are no elements in the list")
#         else:
#             if location == 0:
#                 if self.head == self.tail:
#                     self.head = None
#                     self.tail = None
#                     self.head.next = None
#                     self.head.prev = None
#                 else:
#                     self.head = self.head.next
#                     self.head.prev = self.tail
#                     self.tail.next = self.head
                    
#             elif location == 1:
#                 if self.head == self.tail:
#                     self.head = None
#                     self.tail = None
#                     self.head.next = None
#                     self.head.prev = None
#                 else:
#                     self.tail = self.tail.prev
#                     self.tail.next = self.head   #
#                     self.head.prev = self.tail
#             else:
#                 currNode = self.head
#                 index = 0
#                 while index < location - 1:
#                     currNode = currNode.next
#                     index += 1       
#                 currNode.next = currNode.next.next
#                 currNode.next.prev = currNode

# Delete a CDLL entirely at once
    def deleteCDLL(self):
        if self.head is None:
            print("There are no elements in the list")
        else:
            self.tail.next = None
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("The CDLL has been successfully deleted")

CDLL = CircularDLL()
CDLL.createCDLL(1)
CDLL.insertCDLL(0,0)
CDLL.insertCDLL(1,1)
CDLL.insertCDLL(2,2)
CDLL.insertCDLL(3,3)
CDLL.insertCDLL(4,4)
print([node.value for node in CDLL])
# CDLL.traversalCDLL()
# print([node.value for node in CDLL])
# CDLL.reverseTraversalCDLL()
# print(CDLL.searchCDLL(2))
# print(CDLL.searchCDLL(5))
# CDLL.deleteNodeCDLL(2)
# print([node.value for node in CDLL])
# CDLL.deleteNodeCDLL(3)
# print([node.value for node in CDLL])
# CDLL.deleteNodeCDLL(0)
# print([node.value for node in CDLL])
CDLL.deleteCDLL()
print([node.value for node in CDLL])