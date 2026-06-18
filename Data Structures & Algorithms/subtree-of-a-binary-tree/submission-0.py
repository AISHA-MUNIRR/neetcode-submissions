# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def is_identical(self,p,q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val!=q.val:
                return False
            left=self.is_identical(p.left,q.left)
            right=self.is_identical(p.right,q.right)
            return left and right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        if root.val==subRoot.val:
            if self.is_identical(root,subRoot):
                return True

        left= self.isSubtree(root.left,subRoot)
        right=self.isSubtree(root.right,subRoot)
        return left or right


        

        
        