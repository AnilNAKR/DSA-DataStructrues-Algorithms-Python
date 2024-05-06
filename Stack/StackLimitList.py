class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    # isEmpty()
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    # isFull()
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
    
    # push()
    def push(self, value):
        if self.isFull():
            return "The stack is full"
        else:
            self.list.append(value)
            return "The element has been added to the stack"
        
    # pop()
    def pop(self):
        if self.isEmpty():
            return "The stack is empty":
        else:
            return self.list.pop()
    
    # peak()
    def peak(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.list[len(self.list)-1]

    # Delete
    def delete(self):
        self.list = None
        return "Stack deleted"

customeStack = Stack(3)
print(customeStack.isEmpty())
print(customeStack.isFull())
print('---------------')
customeStack.push(1)
customeStack.push(2)
customeStack.push(3)
print(customeStack.push(4))
print(customeStack)
