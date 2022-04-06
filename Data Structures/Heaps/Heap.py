# Binary Heap - Priority Queue


from multiprocessing.sharedctypes import Value
from operator import index


class BinaryHeap:
    def __init__(self) -> object:
        self.heap = []
        self.size = 0


    def parent(self, index: int):
        # if node is at 'i' location then parent node is at 'i/2' location
        # using flooring function to handle the odd cases : parent at 'floor(i/2)'
        # integer division simulates floor function so need not to use explicitly
        # here index is of the child node or node whose parent we are trying to find

        return self.heap[index//2]

    "For a node left child is at 2*i and right child at 2*i + 1 location respectively"

    def leftChild(self, index: int):
        # index is of the node whose child we are trying to find
        return 2*index
    
    def righChild(self, index):
        # index is of the node whose child we are trying to find
        return 2*index + 1
    
    "If binary heap is maxheap then max element will be the root node and if it is min heap then min element will be root node"
    """So to get:
        max element in max heap: self.heap[1]
        min element in min heap: self.heap[1]"""
    
    def maxHeap(self):
        if self.size == 0:
            raise Exception('Heap is Empty!')    
        return self.heap[1]

    def minHeap(self):
        if self.size == 0:
            raise Exception('Heap is Empty!')
        return self.heap[1]
    
    def percolateDown(self, index):
        # heapifying from root to bottom
         while (index * 2) < self.size:
            # while our child is in the heap
            minChildIndex = self.minHeap()

            if self.heap[index] < self.heap[minChildIndex]:
                # if the node which we are trying to heapify has value less than minnode
                temp = self.heap[index]
                self.heap[index] = self.heap[minChildIndex]
                self.heap[minChildIndex] = temp
            index = minChildIndex

    def percolateUp(self, index):
        # heapifying from bottom to root
        while index//2 > 0:
            if self.heap[index] < self.heap[index//2]:
                temp = self.heap[index//2]
                self.heap[index//2] = self.heap[index]
                self.heap[index] = temp
            index = index//2
    
    def insert(self,value):
        self.heap.append(value)
        self.size += 1
        self.percolateUp(self.size) # heapifying from the elment inserted
    
    def deleteMax(self):
        # delete max element from max heap : root element   
        root = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.percolateDown(1)
        return root
    
    def Min(self):
        # delete min element from min heap : root element   
        root = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.percolateDown(1)
        return root
    