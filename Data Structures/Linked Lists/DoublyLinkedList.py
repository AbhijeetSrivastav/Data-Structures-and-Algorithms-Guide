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
if __name__ == "__main__":
    l = DoublyLinkedList()

    l.insertAtBegining(data=20)
    l.insertAtBegining(data=30)
    l.insertAtEnd(data=100)
    l.insertAtEnd(data=1050)
    l.insertAtPosition(data=26, position=3)



    l.visuzlizelist()