"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from queue import Queue
from stack import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Recursive
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value) # recursive call

        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value) # recursive call

        # Iterative
        # While not at bottom level of tree
        # if value < root, go left
            # if left child is none
                # add here
                #exit loop

        #if value >= root, go right (dupes go to the right)
            # if right child is none
                # add here
                # exit loop

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value and self.left:
            if target == self.left:
                return True
            else:
                return self.left.contains(target)
        if target > self.value and self.right:
            if target == self.right:
                return True
            else:
                return self.right.contains(target)
        return False


    # Return the maximum value found in the tree
    def get_max(self):
        current_node = self
        max_value = self.value
        while current_node.right is not None:
            max_value = current_node.right.value
            current_node = current_node.right
        return max_value
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # one side then the other
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # Recursive - place your print statement in between recursive calls
        # that explore left and right subtrees

        # iterative
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # breadth first using queue
        # iterative
        bft_queue = Queue()
        bft_queue.enqueue(self)
        while bft_queue.__len__() > 0:
            current_node = bft_queue.dequeue()
            # and left child
            if current_node.left:
                bft_queue.enqueue(current_node.left)
            # add right child
            if current_node.right:
                bft_queue.enqueue(current_node.right)
            # dequeue root
            print(current_node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # create a stack to keep track of nodes we are processing
        # push root into stack
        dft_stack = Stack()
        dft_stack.push(self)

        while dft_stack.__len__() > 0:
            # push when we start, pop when a node is done
            current_node = dft_stack.pop()
            print(current_node.value)
            if current_node.left:
                dft_stack.push(current_node.left)
            if current_node.right:
                dft_stack.push(current_node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()
