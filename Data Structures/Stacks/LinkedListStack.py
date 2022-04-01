# Linked List Stack



class Node:
    def __init__(self, data, next) -> object:
        self.data = data
        self.next = next

class Stack:
    def __init__(self) -> object:
        self.head = None


    def sizeOfStack(self):
        if self.head is None:
            raise Exception('Stack is Empty!')
        else:
            size = 0
            currentNode = self.head
            while self.head is not None:
                size += 1
                currentNode = currentNode.next

            return size                
    
    def  visualizeStack(self):
        if self.head is None:
            raise Exception('Stack is Empty!')
        else:
            currentNode = self.head
            ll = ""

            while currentNode is not None: 
                ll = ll + str(currentNode.data) + "-->"
                currentNode = currentNode.next
            print(ll)
    
    def peek(self):
        if self.head is None:
            raise Exception('Stack Underflow!')
        else:
            return self.head.data

    def push(self, data):
        newNode = Node(data, next=None)
        
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    
    def pop(self):
        if self.head is None:
            raise Exception('Stack Underflow!')
        elif self.head.next is None:
            temp = self.head.data
            self.head = None
            return temp
        else:
            temp = self.head.data
            self.head = self.head.next
            return temp