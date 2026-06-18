# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque  # add this at top
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque()
        queue.append(root)
        queue.append(None)
        result=[]
        level=[]

        if not root:
            return []

        while queue:
            curr_node=queue.popleft()
            if curr_node==None:
                result.append(level)
                level=[]
                if not queue:
                    break
                else:
                    queue.append(None)
            else:
                level.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

        return result
        
        