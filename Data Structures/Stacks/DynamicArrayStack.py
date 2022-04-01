# Dynamic Array Stack



class Stack:
    def __init__(self, limit) -> object:
        self.stack = []
        self.limit = limit


    def sizeOfStack(self):
        return len(self.stack)

    def resizeStack(self):
        newStack = list(self.stack)
        self.stack = newStack 
        self.limit = 2 * self.limit
    
    def visualizeStack(self):
        for item in self.stack[::-1]:
            print('-----')
            print('|' + str(item) + '|')
            
    def peek(self):
        if self.sizeOfStack() <= 0:
            raise Exception('Stack is Empty!')
        else:
            return self.stack[-1]

    def push(self, data):
        if self.sizeOfStack() >= self.limit:
            self.resizeStack()
            self.stack.append(data)
        else:
            self.stack.append(data)
    
    def pop(self):
        if self.sizeOfStack() <= 0:
            raise Exception('Stack Underflow!')
        else:
            return self.stack.pop()