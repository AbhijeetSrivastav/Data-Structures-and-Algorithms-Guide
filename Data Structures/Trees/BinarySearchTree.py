# Binary Search Tree



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
    
    def delete(self, value):
        # traverse to the node which has to be deleted
        if value < self.data:
            # then value maybe in left subtree
            if self.left:
                # in left subtree if current node is not leaf node
                # recursively call delete method to reach the node and update the left subtree with new one which is basically subtree without current node
                # else it will return NONE by default
                self.left = self.left.delete(value)
        elif value > self.data:
            # then value maybe in right subtree
            if self.right:
                # in right subtree if current node is not leaf node
                # recursively call delete method to reach the leaf node and update the right subtree with new one which is basically subtree without current node
                # else it will return NONE by default
                self.right = self.right.delete(value)
        else:
            # Case 1: We have no child of node to be deleted
            if self.left is None and self.right is None:
                # node to be delted is leaf node
                # thus return None for it
                return None
            
            # Case 2: We have one child of node to be delted
            elif  self.left is None:
                # if the node to be delted has no left subtree and has only right subtree
                # then return the only child of that node from right subtree 
                # which will replace the node to be delted
                return self.right

            elif self.right is None: 
                # if the node to be deleted has no right subtree and has only left subtree
                # then return the only child of that node from right subtree
                # which will replace the node to be deleted
                return self.left

            # Case 3: We have two child of node to be deleted
            min_value = self.right.minNode()  # copy minimum value from right subtree
            self.data = min_value   # update the value of the node to be deleted(current node) with the min value 
            self.right = self.right.delete(min_value) # delete node with min value as node to be delted is updated with min node

            """Alternate method:  
                max_value = self.right.minNode()  # copy max value from left subtree
                self.data = max_value   # update the value of the node to be deleted(current node) with the max value 
                self.left = self.left.delete(max_value) # delete node with min value as node to be delted is updated with max node"""
        
        return self


def buildBinarySearchTree(elements):
    root = BinarySearchTreeNode(elements[0])

    for element in range(1, len(elements)):
        root.addChild(elements[element])

    return root