 """
Node class to keep track of
the data internal to individual nodes
"""
class Node:
    def __init__(self, parent, key):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None

"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""
class AVLTree:
    def __init__(self, node=None):
        self.node = node
        # init height to -1 because of 0-indexing
        self.height = -1
        self.balance = 0

    """
    Display the whole tree. Uses recursive def.
    """
    def display(self, level=0, pref=''):
        self.update_height()  # Update height before balancing
        self.update_balance()

        if self.node != None: 
            print ('-' * level * 2, pref, self.node.key,
                   f'[{self.height}:{self.balance}]',
                   'L' if self.height == 0 else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.right != None:
                self.node.right.display(level + 1, '>')

    """
    Computes the maximum number of levels there are
    in the tree
    """
    def update_height(self):
        pass

    """
    Updates the balance factor on the AVLTree class
    """
    def update_balance(self):
        pass

    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent. 
    """
    def left_rotate(self, left_child):
        right_child = left_child.right
        right_child.parent = left_child.parent

        if right_child.parent is None:
            self.node = right_child

        else:
            if right_child.parent.left is left_child:
                right_child.parent.left = left_child

            elif right_child.parent.right is left_child:
                right_child.parent.right = right_child

        left_child.right = right_child.left

        if left_child.right is not None:
            left_child.right.parent = left_child

        right_child.left = left_child
        left_child.parent = right_child

        #update the height of left_child

        #update the height of right_child

    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent. 
    """
    def right_rotate(self, right_child):
        
        left_child = right_child.left
        left_child.parent = right_child.parent

        if left_child.parent is None:
            self.node = left_child

        else:
            if left_child.parent.left is right_child:
                left_child.parent.left = left_child

            elif left_child.right is right_child:
                left_child.parent.right = left_child

        right_child.left = left_child.right
        if right_child.left is not None:
            right_child.left.parent = right_child

        left_child.right = right_child
        right_child.parent = left_child

        # update hight of right_child

        #update height of left_child
        
        pass

    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """
    def rebalance(self):
        pass
        
    """
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance
    """
    def insert(self, key):
        if node is None:
            return
        if node.key < self.key:
            if self.left is None:
                self.left = node

            else:
                self.left.insert(node)

        else:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(node)
