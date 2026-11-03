# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p, q):

        # Both nodes are None
        if not p and not q:
            return True

        # One node is None
        if not p or not q:
            return False

        # Compare values and recursively compare children
        if p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # reached leaf
        if not subRoot:
            return True
        # subRoot is not leaf but root is leaf so not identical
        if not root:
            return False
        
        # Check if trees are identical at current node
        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        