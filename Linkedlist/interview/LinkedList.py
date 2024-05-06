from random import randint

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self,value = None):
        self.head = None
        self.tail = None
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next
    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)
    
    def __len__(self):  # provides length of the linked list
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result
    
    def add(self, value):   #Add an element at the end of linked list
        if self.head is None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail
    
    def generate(self,n,min_value,max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value,max_value))
        return self 
 
customLL = LinkedList()
# customLL.generate(10,0,99)
# print(customLL)
# print(len(customLL))
customLL.add(1)
customLL.add(2)
customLL.add(3)
customLL.add(4)
customLL.add(5)
customLL.add(6)
# print([node.value for node in customLL])
# print(len(customLL))
    

