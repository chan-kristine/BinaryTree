class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Data Checking        
    def add_child(self, data):
        if data == self.data:
            return # node already exists

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

# Implement In Order Traversal Function                
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

# Implement Pre-Order Traversal Function   
    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements
  
# Implement Post Order Traversal Function  
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements
 
# Finding Maximum  
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
# Finding Minimum
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()


# Implement Build Tree Function
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    letters = ["K", "R", "I", "S", "T", "I", "N", "E", "A", "G", "C", "A", "Y", "C", "H", "A", "N"]
    letters_tree = build_tree(letters)
    print('╔═*.·:·.✧ ✦ ✧.·:·.**.·:·.✧ ✦ ✧.·:·.**.·:·.✧ ✦ ✧.·:·.**.·:·.✧ ✦ ✧.·:·.**.·:·.✧ ✦ ✧.·:·.**.·:·.✧ ✦ ✧.·:·.*═╗')
    print()
    print("  Given Letters:",letters)
    print()
    print('╚═*.·:·.✧ ✦ ✧.·:·.**.·:·.✧ ✦ ✧.·:·.**.·:·.✧ ✦ ✧.·:·.**.·:·.✧ ✦ ✧.·:·.**.·:·.✧ ✦ ✧.·:·.**.·:·.✧ ✦ ✧.·:·.*═╝')

    print()
    print("\033[01m[1]\33[0m \033[92mMaximum:\33[0m",letters_tree.find_max())
    print("\033[01m[2]\33[0m \033[92mMinimum:\33[0m",letters_tree.find_min())
    print("\033[01m[3]\33[0m \033[92mIn Order Traversal sorted list:\33[0m",letters_tree.in_order_traversal())
    print("\033[01m[4]\33[0m \033[92mPre-Order Traversal sorted list:\33[0m",letters_tree.pre_order_traversal())
    print("\033[01m[5]\33[0m \033[92mPost Order Traversal sorted list:\33[0m",letters_tree.post_order_traversal())

    

    