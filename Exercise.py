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

# Implement Search Function    
    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
                        
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
# Implement Pre Order Traversal Method
    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements
 
# Implement Post Order Traversal Method   
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

# Finding Maximum Number   
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

# Finding MInimum Number
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

#Calculating the Sum of all given numbers 
    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum
    
def build_tree(elements):
        root = BinarySearchTreeNode(elements[0])

        for i in range(1,len(elements)):
            root.add_child(elements[i])

        return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print("Input numbers:",numbers)
    print("Min:",numbers_tree.find_min())
    print("Max:",numbers_tree.find_max())
    print("Sum:", numbers_tree.calculate_sum())
    print("Does number 3 exist in the list?", numbers_tree.search(3))
    print("Does number 17 exist in the list?", numbers_tree.search(17))
    print("In order traversal:", numbers_tree.in_order_traversal())
    print("Pre order traversal:", numbers_tree.pre_order_traversal())
    print("Pre order traversal:", numbers_tree.post_order_traversal())
 
 
# Reference: Practice Exercise - https://youtu.be/lFq5mYUWEBk