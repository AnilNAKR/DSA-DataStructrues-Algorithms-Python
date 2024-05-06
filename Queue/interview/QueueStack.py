class Stack:
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)
    
    def push(self,value):
        self.list.append(value)

    def pop(self):
        if len(self.list) == 0:
            return None
        return self.list.pop()
    
class Queue:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    def enqueue(self,value):
        self.inStack.push(value)

    def dequeue(self):
        while len(self.inStack):
            self.outStack.push(self.inStack.pop())
        result = self.outStack.pop()
        while len(self.outStack):
            self.inStack.push(self.outStack.pop())
        return result
    

customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.dequeue())
    