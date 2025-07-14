class Solution:
    def exist(self, board: List[List[str]], word: str):
        rows, cols = len(board), len(board[0])

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    # Stack holds (row, col, index_in_word, visited_set)
                    stack = [(i, j, 0, set([(i, j)]))]

                    while stack:
                        row, col, index, visited = stack.pop()

                        # ✅ If entire word matched
                        if index == len(word) - 1:
                            return True

                        # 🔁 Explore all 4 directions
                        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                            new_r, new_c = row + dr, col + dc
                            if (
                                0 <= new_r < rows and
                                0 <= new_c < cols and
                                (new_r, new_c) not in visited and
                                board[new_r][new_c] == word[index + 1]
                            ):
                                new_visited = visited.copy()
                                new_visited.add((new_r, new_c))
                                stack.append((new_r, new_c, index + 1, new_visited))

        return False
    
    def chatsolution(board, word):
        rows, cols = len(board), len(board[0])

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    # Stack holds (row, col, index_in_word, visited_set)
                    stack = [(i, j, 0, set([(i, j)]))]

                    while stack:
                        row, col, index, visited = stack.pop()

                        # ✅ If entire word matched
                        if index == len(word) - 1:
                            return True

                        # 🔁 Explore all 4 directions
                        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                            new_r, new_c = row + dr, col + dc
                            if (
                                0 <= new_r < rows and
                                0 <= new_c < cols and
                                (new_r, new_c) not in visited and
                                board[new_r][new_c] == word[index + 1]
                            ):
                                new_visited = visited.copy()
                                new_visited.add((new_r, new_c))
                                stack.append((new_r, new_c, index + 1, new_visited))

        return False 
