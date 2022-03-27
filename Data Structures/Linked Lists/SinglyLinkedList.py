# Singly Linked List

from json.tool import main
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
            
            print(length)
    
    def insertAtBegining(self, data, next=None):
        newNode = Node(data, next=None)
        
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
            

if __name__ == "__main__":
    l = SinglyLinkedList()
    
    l.insertAtBegining(data=20)
    l.insertAtBegining(data=30)
    l.insertAtBegining(data=40)
    l.insertAtBegining(data=50)
    l.listLength()
    

    l.visuzlizelist()