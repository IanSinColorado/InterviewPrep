# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree(object):
    def __init__(self, node=None):
        self.root = node

    # REturn a path of how it got there
    def DFS(self, node, path, searchVal):
        if node.val == None:
            return None
        if searchVal == node.val:
            return path
        if node.left != None:
            path.append("L")
            self.DFS(node.left, path, searchVal)
        if node.right != None:
            path.append("R")
            self.DFS(node.right, path, searchVal)
        
    # returns a path
    def search(self, searchVal, searchFunc):
        return searchFunc(searchVal)


    def preOrder(self):
        return None