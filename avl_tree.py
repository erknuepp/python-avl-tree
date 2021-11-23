# AVLTree: A Self-balancing Binary Search Tree
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_avl_tree.py.
# Do not modify the starter code provided.
# YOUR NAME

class AVLTree:


    #Add additional methods as needed. Use the helper methods provided below.
    def __init__(self, key: int = None) -> None:
        self.balance_factor = 0
        self.key = key
        self.left = None
        self.parent = None
        self.right = None

    # You will need to modify this method
    def insert(self, node):
        if node.key <= self.key:
            if not self.has_left_child():
                self.left = node
                node.parent=self 
            else:
                self.left.insert(node)
        else:
            if not self.has_right_child():
                self.right = node
                node.parent = self 
            else:
                self.right.insert(node) 
    
    # Do not modify these helper functions. They are included for your convenience,
    def _is_left_child(self):
            return self.parent.left is self

    def _is_right_child(self):
            return self.parent.right is self

    def _is_root_node(self):
            return self.parent is None
 
    def is_leaf(self):
            return not (self.has_left_child() or self.has_right_child())

    def has_left_child(self):
        return not self.left is None

    def has_right_child(self):
        return not self.right is None

    def has_left_child_only(self):
        return not self.left is None and self.right is None

    def has_right_child_only(self):
        return not self.right is None and self.left is None
   
    
   