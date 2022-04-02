# Singly Linked List Implementation of Queue



class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    
    def visualizeQueue(self):
        if self.front == self.rear == None:
            raise Exception('Queue is Empty!')
        else:
            currentNode = self.front
            ll = ""

            while currentNode is not None: 
                ll = ll + str(currentNode.data) + "-->"
                currentNode = currentNode.next
            print(ll)

    def Enqueue(self,data):
        if self.rear is None:
            self.front = self.rear = Node(data)
        else:
            self.rear.next = Node(data)
            self.rear = self.rear.next
            
    def Dequeue(self):
        if self.front is None:
            raise Exception('Queue Underflow!')
        else:
            to_return = self.front.data
            self.front = self.front.next
            return to_return
        
    def IsEmpty(self):
        return self.front is None
    
    def Size(self):
        count = 0
        cur = self.front
        while(cur):
            count+=1
            cur = cur.next
        return count
    
    def Front(self):
        return self.front.data
    
    def Rear(self):
        return self.rear.data