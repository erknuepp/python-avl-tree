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
        
    def _height(self):
        if(self.is_leaf()):
            leftHeight = 0
            rightHeight = 0
        else:
            leftHeight = self.left._height() + 1 if self.has_left_child() else 0
            rightHeight = self.right._height() + 1 if self.has_right_child() else 0
        return max(leftHeight, rightHeight)

    # private helper methods
    def _caculateBalanceFactor(self, height) -> int:
        
        if self._is_root_node:
            return
        elif self._is_left_child:
            self.parent.balance_factor = self._height() - (self.parent.right._height if self.parent.has_right_child else 0)
        else:
            self.parent.balance_factor = (self.parent.left._height() if self.parent.has_left_child else 0) - self._height()
        
        self.parent._caculateBalanceFactor(height)
        
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
        self._caculateBalanceFactor(0)
    

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
   
    
   