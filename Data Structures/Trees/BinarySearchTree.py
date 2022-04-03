# Binary Search Tree




from turtle import left


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def addChild(self, data):
        if data == self.data:
            # Child already Present! Duplicay Not Allowed!
            return
        
        if data < self.data:
            # add to left subtree
            if self.left:
                # current node is not leaf node
                # recursively call addChild to reach the leaf node
                self.left.addChild(data)
            else:
                # current node is leaf node 
                # add new node to it
                self.left = BinarySearchTreeNode(data)
        else:
            #add to right subtree
            if self.right:
                # current node is not leaf node
                # recursively call addChild to reach the leaf node
                self.right.addChild(data)
            else:
                # current node is leaf node
                # add new node to it
                self.right = BinarySearchTreeNode(data)
        
    def searchValue(self, value):
        if self.data == value:
            return True
        
        if value < self.data:
            # value maybe in left subtree
            if self.left:
                # current node is not leaf node
                # recursively call searchValue to reach the leaf node
                self.left.searchValue(value)
            else:
                # current node is leaf node
                # then value is not in left subtree
                return False

        if value > self.data:
            # value maybe in right subtree 
            if self.right:
                # current node is not leaf node
                # recursively call searchValue to reach the leaf node
                self.right.searchValue(value)
            else:
                # current node is leaf node
                # then value is not in the right subtree
                return False
        
    def inOrderTraversal(self):
        # left-root-right
        inOrderTraversalSequence = []

        if self.left:
            # in left subtree if current node is not leaf node 
            # recursively call inOrderTraversal to reach the leaf node
            # at each recurssion we are adding the new sequence to old one
            inOrderTraversalSequence += self.left.inOrderTraversal()
        
        # at base node update the sequence with current node data
        inOrderTraversalSequence.append(self.data)

        if self.right:
            # in right subtree if current node is not leaf node
            # recursively call inOrderTraversal to reach the leaf node
            # at each recurssion we are adding the new sequence to old one
            inOrderTraversalSequence += self.right.inOrderTraversal()
    
        return inOrderTraversalSequence
    
    def preOrderTraversal(self):
        # root-left-right
        preOrderTraversalSequence = []

        # at base node update the sequence with current node data
        preOrderTraversalSequence.append(self.data)

        if self.left:
            # in left subtree if current node is not leaf node
            # recursively call preOrderTraversalSequence to reach the leaf node
            # at each recurssion we are adding the new sequence to old one
            preOrderTraversalSequence += self.left.preOrderTraversal()
        
        if self.right:
            # in right subtree if current node is not leaf node
            # recursively call inOrderTraversal to reach the leaf node
            # at each recurssion we are adding the new sequence to old one
            preOrderTraversalSequence += self.right.preOrderTraversal()
        
        return preOrderTraversalSequence
    
    def postOrderTraversal(self):
        # left-right-root
        postOrderTraversalSequence = []
        
        if self.left:
            # in left subtree if current node is not leaf node
            # recursively call postOrderTraversal to reach the leaf node
            # at each recurssion we are adding the new sequence to old one
            postOrderTraversalSequence += self.left.postOrderTraversal()
        
        if self.right:
            # in right subtree if current node is not leaf node
            # recursively call postOrderTraversal to reach the leaf node
            # at each recurssion we are adding the new sequence to old one
            postOrderTraversalSequence += self.right.postOrderTraversal()
        
        # at base condtion append the current node data to postOrderTraversalSequence
        postOrderTraversalSequence.append(self.data)
    
        return postOrderTraversalSequence
            
    def minNode(self):
        "Alternate way: return self.postOrderTraversal()[0]"
        if self.left is None:
            # if leaf node       
            return self.data
        return self.left.minNode()

    def maxNode(self):
        "Alternate way: return self.inOrderTraversal()[-1]"
        if self.right is None:
            # if leaf node
           return self.data
        return  self.right.maxNode()

    def sumNode(self):
        "Alternate way: sum the elements of any traversal sequence"
        left_sum = self.left.sumNode() if self.left else 0
        right_sum = self.right.sumNode() if self.right else 0
        return self.data + left_sum + right_sum       

def buildBinarySearchTree(elements):
    root = BinarySearchTreeNode(elements[0])

    for element in range(1, len(elements)):
        root.addChild(elements[element])

    return root
    
if __name__ == "__main__":
    # countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    # country_tree = buildBinarySearchTree(countries)

    # print("UK is in the list? ", country_tree.searchValue("UK"))
    # print("Sweden is in the list? ", country_tree.searchValue("Sweden"))

    numbers_tree = buildBinarySearchTree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:",numbers_tree.inOrderTraversal())
    print("Post order traversal gives this sorted list:",numbers_tree.postOrderTraversal())   
    print("Pre order traversal gives this sorted list:",numbers_tree.preOrderTraversal())
    print(numbers_tree.maxNode())
    print(numbers_tree.minNode())
    print(numbers_tree.sumNode())
    
