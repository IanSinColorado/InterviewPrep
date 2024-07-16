# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def LCA(self, node, p, q):
        if node == None:
            return node
        
        leftSide = self.LCA(node.left, p, q)
        rightSide = self.LCA(node.right, p, q)

        if( (leftSide and rightSide) or (node.val == p or node.val == q) ):
            return node
        if leftSide == None:
            return rightSide
        else:
            return leftSide

    lcaToStart = ""
    lcaToEnd = ""
    def DFS(self, node, pathString, p, q):
        if(node == None):
            return
        if node.val == p:
            self.lcaToStart = pathString
        if node.val == q:
            self.lcaToEnd = pathString

        pathString += "L"
        self.DFS(node.left, pathString, p, q)
        pathString = pathString[:len(pathString)-1]

        pathString += "R"
        self.DFS(node.right, pathString, p, q)
        pathString = pathString[:len(pathString)-1]


    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        lcaNode = self.LCA(root, startValue, destValue)

        pathString = ""
        self.DFS(lcaNode, pathString, startValue, destValue)

        self.lcaToStart = "U" * len(self.lcaToStart)
        
        return self.lcaToStart + self.lcaToEnd



# Not worrying about Least Common Ancestor (LCA)
# Two pointers: one for the root->start and the other for root->dest
class Solution:
    rootToStart = ""
    rootToEnd = ""

    def DFS(self, node, pathString, p, q):
        if(node == None):
            return
        if node.val == p:
            self.rootToStart = pathString
        if node.val == q:
            self.rootToEnd = pathString

        pathString += "L"
        self.DFS(node.left, pathString, p, q)
        pathString = pathString[:len(pathString)-1]

        pathString += "R"
        self.DFS(node.right, pathString, p, q)
        pathString = pathString[:len(pathString)-1]


    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.DFS(root, "", startValue, destValue)

        counter = 0
        i = 0
        j = 0
        while i < len(self.rootToStart) and j < len(self.rootToEnd):
            if self.rootToStart[i] == self.rootToEnd[j]:
                i += 1
                j += 1
                counter += 1
            else:
                break

        return self.rootToStart[counter:] + self.rootToEnd[counter:]