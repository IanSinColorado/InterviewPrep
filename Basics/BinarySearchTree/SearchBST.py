# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree(object):
    def __init__(self, node=None):
        self.root = node


    def preOrder(self):
        return None