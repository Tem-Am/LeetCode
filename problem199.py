# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import deque
class Solution:
    def rightSideView(self, root):
        # Same idea of bfs and end of each level add to answer of node
        # Base case, where tree is empty
        if not root:
            return []
        else:
            # It means root exist, not a null
            ans = [] # store all right side nodes
            q = deque()
            q.append(root)
            while q:
                total_nodes = len(q) # size of it 
                for _ in range(total_nodes):
                    node = q.popleft() # the first element

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                ans.append(node.val)
        return ans
