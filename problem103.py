# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        turn = True # if true mean left, and false mean right 
        # same idea here -> bfs
        # base case
        if not root:
            return []
        else:
            # add values from left to right
            q = deque() # queue and stack usage for bfs
            q.append(root)
            while q:
                values = []
                totalnodes = len(q) # total nodes in that level
                for _ in range(totalnodes):
                    node = q.popleft()
                    values.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right: 
                        q.append(node.right)
                if not turn:
                    values.reverse()
                answer.append(values)
                turn = not turn # reverse for zigzag input
        return answer