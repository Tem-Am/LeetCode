import List
from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int):
        # Not a greedy search because no range
        # left -> i - arr[i],  right -> i + arr[i]
        # Cannot out a range of arr
        # Base case
        if len(arr) == 1:
            return True
        if arr[start] == 0:
            return True
        
        q = deque() # add all possible jumps
        q.append(start)
        known = {start}
        while q:
            current = q.popleft()
            if arr[current] == 0:
                return True
            # From the top, need to know left and right index
            left = current - arr[current]
            right = current + arr[current]

            if 0 <= left and right < len(arr) and left not in known and right not in known:
                q.append(left)
                q.append(right)
                known.add(left)
                known.add(right)
            elif right < len(arr) and right not in known:
                q.append(right)
                known.add(right)
            elif 0 <= left and left not in known:
                q.append(left)
                known.add(left)

        return False