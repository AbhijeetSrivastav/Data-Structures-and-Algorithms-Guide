#Doubly Linked List


class Node:
    def __init__(self, data, next, prev) -> object:
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self) -> object:
        self.head = None

    
    def visuzlizelist(self):
        if self.head is None:
            raise Exception('List is Empty!')
        else:
            currentNode = self.head
            ll = ""

            while currentNode is not None: 
                ll = ll + str(currentNode.data) + "<-->"
                currentNode = currentNode.next
            print(ll)

    def listLength(self):
        length = 0
        if self.head is None:
            return length
        else:
            currentNode = self.head
            while currentNode is not None:
                length += 1
                currentNode = currentNode.next
        
        return length

    
    def insertAtBegining(self, data):
        newNode = Node(data, next=None, prev=None)

        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            newNode.prev = None
            self.head = newNode

    def insertAtEnd(self, data):
        newNode = Node(data, next=None, prev=None)

        if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head

            while currentNode.next is not None:
                currentNode = currentNode.next
            
            currentNode.next = newNode
            newNode.next = None
            newNode.prev = currentNode

    def insertAtPosition(self, data, position):
        if position < 0 or position > self.listLength():
            raise Exception('Invalid Position!')
        elif position == 0:
            self.insertAtBegining(data)
        elif position == self.listLength():
            self.insertAtEnd(data)
        else:
            newNode = Node(data, next=None, prev=None)
            currentNode = self.head
            count = 0

            while currentNode.next is not None:
                if count == position - 1:
                    newNode.next = currentNode.next
                    newNode.prev = currentNode
                    currentNode.next.prev = newNode
                    currentNode.next = newNode
                
                count += 1
                currentNode = currentNode.next

    def deleteFromBegining(self):
        if self.head is None:
            raise Exception('List is Empty!')
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def deleteFromEnd(self):
        if self.head is None:
            raise Exception('List is Empty!')
        elif self.head.next is None:
            self.head = None
        else:
            currentNode = self.head

            while currentNode.next is not None:
                currentNode = currentNode.next
            
            currentNode.prev.next = None

    def deleteFromPositon(self, position):
        if position < 0 or position > self.listLength():
            raise Exception('Invalid Positon!')
        elif position == 0:
            self.deleteFromBegining()
        elif position == self.listLength():
            self.deleteFromEnd()
        else:
            count = 0
            currentNode = self.head

            while currentNode.next is not None:
                if count == position - 1:
                    currentNode.next = currentNode.next.next
                    currentNode.next.prev = currentNode
                
                count +=1
                currentNode = currentNode.next