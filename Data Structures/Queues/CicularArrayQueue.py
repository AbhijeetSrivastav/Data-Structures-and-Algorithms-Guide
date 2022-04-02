# Cicular Array Queue Implementation



class CicularArrayQueue:
    def __init__(self, size) -> None:
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    
    def visualizeQueue(self):
        if(self.front == -1):
            raise Exception('Queue Underflow!')
        elif (self.rear >= self.front):
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.front, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

    def enqueue(self, data):
        if ((self.rear + 1) % self.size == self.front):
            raise Exception('Queue Overflow!')
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data
    
    def dequeue(self):
        if self.front == -1:
            raise Exception('Queue Underflow!')
        elif self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size