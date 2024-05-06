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
    
    # # Traversing Double Linked List
    # def traverseDLL(self):
    #     if self.head is None:
    #         print("There is not any element to traverse")
    #     else:
    #         tempNode = self.head
    #         while tempNode:
    #             print(tempNode.value)
    #             tempNode = tempNode.next
    
    # # Reverse Traversal of DLL
    # def RtraverseDLL(self):
    #     if self.head is None:
    #         print("There is no element to traverse")
    #     else:
    #         tempNode1 = self.tail
    #         while tempNode1:
    #             print(tempNode1.value)
    #             tempNode1 = tempNode1.prev

# # Searching for a node value in DLL
#     def searchDLL(self, Svalue):
#         if self.head is None:
#             print("There are no elements in the list")
#         else:
#             tempNode = self.head
#             while tempNode:
#                 if tempNode.value == Svalue:
#                     return tempNode.value
#                 tempNode = tempNode.next
#             return "The node does not exist in this list"
        
# # Deletion of a node in DLL
#     def deleteNodeDLL(self, location):
#         if self.head is None:
#             print("There are no elements in the list")
#         else:
#             if location == 0:
#                 if self.head == self.tail:
#                     self.head = None
#                     self.tail = None
#                 else:
#                     node = self.head # or self.head = self.head.next and self.head.prev = None
#                     node.next.prev = None
#                     self.head = node.next
#             elif location == 1:
#                 if self.head == self.tail:
#                     self.head = None
#                     self.tail = None
#                 else:
#                     self.tail = self.tail.prev
#                     self.tail.next = None
#             else:
#                 curNode = self.head
#                 index = 0
#                 while index < location - 1:
#                     curNode = curNode.next
#                     index += 1
#                 nextNode = curNode.next
#                 curNode.next = nextNode.next
#                 nextNode.prev = curNode
#                 nextNode.next = None
#             print("The node has been successfully deleted")

# Deletion of entire List
    def deleteDLL(self):
        if self.head is None:
            print("There is not any node in DLL")
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("The DLL has been successfully deleted")  

DoubleLL = DoubleLinkedList()
DoubleLL.creationDLL(5)
DoubleLL.insertDLL(0,0)
DoubleLL.insertDLL(1,1)
DoubleLL.insertDLL(2,2)
DoubleLL.insertDLL(3,3)
DoubleLL.insertDLL(4,4)
DoubleLL.insertDLL(4,4)
DoubleLL.insertDLL(7,3)


print([node.value for node in DoubleLL])
# DoubleLL.traverseDLL()
# DoubleLL.RtraverseDLL()
# print(DoubleLL.searchDLL(7))
# print(DoubleLL.searchDLL(1))
# print(DoubleLL.searchDLL(6))
# DoubleLL.deleteNodeDLL(0)
# print([node.value for node in DoubleLL])
# DoubleLL.deleteNodeDLL(1)
# print([node.value for node in DoubleLL])
# DoubleLL.deleteNodeDLL(2)      
# print([node.value for node in DoubleLL])
# DoubleLL.deleteNodeDLL(3)      
# print([node.value for node in DoubleLL])
DoubleLL.deleteDLL()
print([node.value for node in DoubleLL])