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
    # insert in Linked List
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
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

    # # Traverse Single Linked List
    # def traverseSLL(self):
    #     if self.head is None:
    #         print("The Single Linked List does not exist")
    #     else:
    #         node = self.head
    #         while node is not None:
    #             print(node.value)
    #             node = node.next

    # Search for a node in Single Linked List
    def searchSLL(self, nodeValue):
        if self.head is None:
            return "The List does not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The value does not exist in this list"

sLinkedList = SingleLinkedList()
sLinkedList.insertSLL(1, 1)
sLinkedList.insertSLL(2, 1)
sLinkedList.insertSLL(3, 1)
sLinkedList.insertSLL(4, 1)
sLinkedList.insertSLL(2, 0)
sLinkedList.insertSLL(7, 4)
sLinkedList.insertSLL(0, 0)
print([node.value for node in sLinkedList])
# sLinkedList.traverseSLL()
print(sLinkedList.searchSLL(7))
print(sLinkedList.searchSLL(4))
