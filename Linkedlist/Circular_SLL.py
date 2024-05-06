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
            if node.next == self.head:
                break
            node = node.next
    
    # Create of cicular Single Linked List
    def createCSLL(self, nodevalue):
        node = Node(nodevalue)
        node.next = node
        self.head = node
        self.tail = node
        return "The circular single linked list has been created"

cicularSLL = CicularSingleLinkedList()
cicularSLL.createCSLL(1) # or print(cicularSLL.createCSLL(1)) - for printing the return message


print([node.value for node in cicularSLL])