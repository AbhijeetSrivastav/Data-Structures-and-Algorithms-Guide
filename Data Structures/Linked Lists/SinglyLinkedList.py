# Singly Linked List

from msilib.schema import Error


class Node:
    def __init__(self, data, next) -> object:
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self) -> object:
        self.head = None
    
    
    def visuzlizelist(self):
        if self.head is None:
            raise Exception('List is Empty!')
        else:
            currentNode = self.head
            ll = ""

            while currentNode is not None: 
                ll = ll + str(currentNode.data) + "-->"
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
        newNode = Node(data, next=None)
        
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
            
    def insertAtEnd(self, data):
        newNode = Node(data, next=None)

        if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            
            currentNode.next = newNode
            newNode.next = None

    def insertAtPosition(self, data, position: int):
        if position < 0 or position > self.listLength():
            raise Exception('Invalid Position!')
        elif position == 0:
            self.insertAtBegining(data)
        elif position == self.listLength():
            self.insertAtEnd(data)
        else:
            newNode = Node(data, next=None)
            currentNode = self.head
            count = 0

            while currentNode.next is not None:
                if count == position - 1:
                    newNode.next = currentNode.next
                    currentNode.next = newNode
                
                count += 1
                currentNode = currentNode.next

    def deleteFromBegining(self):
        if self.head is None:
           raise Exception('List is Empty!')
        else:
            self.head = self.head.next 
    
    def deleteFromEnd(self):
        if self.head is None:
            raise Exception('List is Empty!')
        else:
            currentNode = self.head
            previousNode = self.head
            while currentNode.next is not None:
                previousNode = currentNode
                currentNode = currentNode.next
            
            previousNode.next = None

    def deletefromPosition(self, position):
        if position < 0 or position > self.listLength():
           raise Exception('Invalid Position!')      
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
                    break

                count += 1
                currentNode = currentNode.next 

                