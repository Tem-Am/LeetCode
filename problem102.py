# Definition for a binary tree nodes.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import deque
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        
        # Check left and right and pop it and add to answer
        q = deque() # We can check right side first and then left side
        ans = []
        if root:
            q.append(root)
            while q:
                length = len(q)
                nodes_vals = []
                for _ in range(length):
                    node = q.popleft() # get the first elemnt in q
                    nodes_vals.append(node.val)

                    # Check two sides
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                ans.append(nodes_vals)
        return ans