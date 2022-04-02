# Linear Array Queue Implementation


"""USING LIST"""

class LinearArrayQueue_TYPE1:
    def __init__(self) -> object:
        self.queue = []
    
    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        self.queue.pop()
    
    def visualizeQueue(self):
        print(self.queue)

    def size(self):
        return len(self.queue)
    
    def front(self):
        return self.queue[0]
    
    def rear(self):
        return self.queue[-1]
    

"""USING collections.dequeue"""

from collections import deque

class LinearArrayQueue_TYPE2:
    def __init__(self) -> object:
        self.queue = deque()
    
    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        self.queue.popleft()
    
    def visualizeQueue(self):
        print(self.queue)

    def size(self):
        return len(self.queue)
    
    def front(self):
        return self.queue[0]
    
    def rear(self):
        return self.queue[-1]

if __name__ == "__main__":
    q = LinearArrayQueue_TYPE2()

    q.enqueue(20)
    q.enqueue(200)
    q.enqueue(2000)
    q.enqueue(20000)
    print(q.front())
    print(q.rear())

    q.visualizeQueue()