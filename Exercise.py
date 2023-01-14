class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
# Data Checking
    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            # add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

# Implement In Order Traversal Method
    def in_order_traversal(self):
        elements = []

        # visit the left tree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit the base node
        elements.append(self.data)

        # visit the right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements
            
