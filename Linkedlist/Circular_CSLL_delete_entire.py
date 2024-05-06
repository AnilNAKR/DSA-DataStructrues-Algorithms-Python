class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None

class CicularSingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            # if node.next == self.head:
            #     break
            # node = node.next
            node = node.next
            if node == self.tail.next:
                break

    # Create of cicular Single Linked List
    def createCSLL(self, nodevalue):
        node = Node(nodevalue)
        node.next = node
        self.head = node
        self.tail = node
        return "The circular single linked list has been created"

    # Insertion of a node in CSLL
    def insertCLL(self, value, location):
        if self.head is None:
            return "The head reference is None"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return "The node has been successfully inserted"
        
    # # Traversal Circular SLL
    # def traversalCSLL(self):
    #     if self.head is None:
    #         print("There is not any element for traversal")
    #     else:
    #         tempNode = self.head
    #         while tempNode:
    #             print(tempNode.value)
    #             tempNode = tempNode.next
    #             if tempNode == self.tail.next:
    #                 break

    # # Searching for a node in a circular single linked list
    # def searchCSLL(self, nodeValue):
    #     if self.head is None:
    #         return "There is not any node in this CSLL"
    #     else:
    #         tempNode = self.head
    #         while tempNode:
    #             if tempNode.value == nodeValue:
    #                 return tempNode.value
    #             tempNode = tempNode.next
    #             if tempNode == self.tail.next:
    #                 return "The node does not exist in this CSLL"

    # # Delete a node from the CSLL
    # def deletionNodeCSLL(self, location):
    #     if self.head is None:
    #         print("There is not any node in CSLL")
    #     else:
    #         if location == 0:
    #             if self.head == self.tail:
    #                 self.head.next = None
    #                 self.head = None
    #                 self.tail = None                    
    #             else:
    #                 self.head = self.head.next
    #                 self.tail.next = self.head
    #         elif location == 1:
    #             if self.head == self.tail:
    #                 self.head.next = None
    #                 self.head = None
    #                 self.tail = None
    #             else:
    #                 tempNode = self.head
    #                 while tempNode is not None:
    #                     if tempNode.next == self.tail:
    #                         break
    #                     tempNode = tempNode.next
    #                 tempNode.next = self.head
    #                 self.tail = tempNode
    #         else:
    #             tempNode1 = self.head
    #             index = 0
    #             while index < location - 1:
    #                 tempNode1 = tempNode1.next
    #                 index += 1
    #             nextNode = tempNode1.next
    #             tempNode1.next = nextNode.next

    # Delete entire Circular Single Linked List
    def deleteEntireCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None


cicularSLL = CicularSingleLinkedList()
cicularSLL.createCSLL(1) # or print(cicularSLL.createCSLL(1)) - for printing the return message
cicularSLL.insertCLL(0,0)
cicularSLL.insertCLL(2,1)
cicularSLL.insertCLL(3,1)
cicularSLL.insertCLL(4,2)
print([node.value for node in cicularSLL])
# cicularSLL.traversalCSLL()
# print(cicularSLL.searchCSLL(3))
# cicularSLL.deletionNodeCSLL(2)
cicularSLL.deleteEntireCSLL()

print([node.value for node in cicularSLL])
