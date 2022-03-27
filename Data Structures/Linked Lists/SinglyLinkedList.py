# Singly Linked List

from json.tool import main
from tkinter.messagebox import NO
from tkinter.tix import MAIN


class Node:
    def __init__(self, data, next) -> object:
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self) -> object:
        self.head = None
    
    def visuzlizelist(self):
        if self.head is None:
            print('Linked List is Empty!')
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
            print('Invalid Position!')
        elif position == 0:
            self.insertAtBegining(data)
        elif position == self.listLength():
            self.insertAtEnd(data)
        else:
            newNode = Node(data, next=None)
            currentNode = self.head
            count = 0

            while currentNode.next is not None:
                count += 1
                currentNode = currentNode.next
                
                if count == position - 1:
                    newNode.next = currentNode.next
                    currentNode.next = newNode


            


if __name__ == "__main__":
    l = SinglyLinkedList()
    
    l.insertAtBegining(data=20)
    l.insertAtBegining(data=30)
    l.insertAtBegining(data=40)
    l.insertAtBegining(data=50)
    l.insertAtEnd(data=100)
    l.insertAtEnd(data=60)

    l.insertAtPosition(data=99, position=2)
    

    l.visuzlizelist()