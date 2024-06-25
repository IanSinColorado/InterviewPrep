# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive
class Solution:
    globalSum = 0
    def solve(self, node):
        if node == None:
            return
        
        self.solve(node.right)
        globalSum += node.val
        node.val = globalSum
        self.solve(node.left)

        return
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        globalSum = 0
        self.solve(root)
        return root


# Iterative Solution
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        globalSum = 0
        stack = []
        curr = root

        while(curr != None or len(stack) != 0):
            while(curr != None):
                stack.append(curr)
                curr = curr.right
            
            curr = stack.pop()
            globalSum += curr.val
            curr.val = globalSum
            curr = curr.left

        return root


# Morris Traversal (Reversed)
class Solution:
    globalSum = 0
    def postExtremeLeftFunc(self, node):
        post = node.right
        while(post.left != None and post.left != node):
            post = post.left
        return post
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        globalSum = 0
        node = root

        while node != None:
            post = node.right
            if post == None:
                globalSum += node.val
                node.val = globalSum
                node = node.right
            else:
                postExtremeLeft = self.postExtremeLeftFunc(node)
                
                if postExtremeLeft.left == None:
                    postExtremeLeft.left = node
                    node = node.right
                else:
                    postExtremeLeft.left = None
                    globalSum += node.val
                    node.val = globalSum
                    node = node.left

        return root