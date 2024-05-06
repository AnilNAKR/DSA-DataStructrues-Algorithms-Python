class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
       values = [str(x) for x in self.items]
       return " ".join(values)
    
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
    
    # Amortized Time constant - for memory allocation when the default size to be extended
    def enqueue(self, value):
        self.items.append(value)
        return "The element is inserted at the end of the queue"

    def dequeue(self):
        if self.isEmpty():
            return "There are no elements in the Queue"
        else:
            return self.items.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "There are no elements in the Queue"
        else:
            return self.items[0]
        
    def delete(self):
        self.items = None

if __name__ == "__main__":
    customQueue = Queue()
    print(customQueue.isEmpty())
    customQueue.enqueue(1)
    customQueue.enqueue(2)
    customQueue.enqueue(3)
    print(customQueue)
    # print(customQueue.dequeue())
    print(customQueue.peek())
    # print(customQueue)