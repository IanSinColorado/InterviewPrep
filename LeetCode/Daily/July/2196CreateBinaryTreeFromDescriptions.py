# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):        
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        hasParent = {}
        for desc in descriptions:
            parentVal = desc[0]
            childVal = desc[1]
            isLeft = desc[2]

            parentNode = None
            childNode = None

            if parentVal in nodes.keys():
                parentNode = nodes[parentVal]
            else:
                nodes[parentVal] = TreeNode(parentVal)
                parentNode = nodes[parentVal]

            if childVal in nodes.keys():
                childNode = nodes[childVal]
            else:
                nodes[childVal] = TreeNode(childVal)
                childNode = nodes[childVal]

            if isLeft:
                parentNode.left = childNode
            else:
                parentNode.right = childNode

            hasParent[childVal] = True
            nodes[childVal] = childNode
            nodes[parentVal] = parentNode

        for item in nodes.items():
            try:
                truth = hasParent[item[0]]
            except:
                return item[1]




            