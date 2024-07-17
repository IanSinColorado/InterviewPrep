# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    rootNodes = []
    def DFS(self, node, to_delete, root_truth):
        if(node == None):
            return

        if node.val in to_delete:
            self.DFS(node.left, to_delete, True)
            self.DFS(node.right, to_delete, True)
        else:
            if root_truth:
                self.rootNodes.append(node)

            n_left = node.left
            n_right = node.right

            if node.left != None:
                if node.left.val in to_delete:
                    node.left = None

            if node.right != None:
                if node.right.val in to_delete:
                    node.right = None
            
            self.DFS(n_left, to_delete, False)
            self.DFS(n_right, to_delete, False)


    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.rootNodes.clear()
        self.DFS(root, to_delete, True)
        return self.rootNodes