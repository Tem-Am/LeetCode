def uniquePaths(m,  n):
    # (0,0) is roboot
    # (m-1, n-1)
    # Create 2D grid to save each possible way to come to each node
    #matrix = [[ 0 for _ in range(n)] for _ in range(m)]
    # Matrix --> [[]]
    matrix = []           
    for i in range(m):
        matrix.append([])
        for j in range(n):
            if i == 0:
                matrix[i].append(1)
            elif j == 0 and i != 0:
                matrix[i].append(1)
            else:
                matrix[i].append(0)
    # down and right will be added into each node
    # we will move only down and right
    for down in range(1, m):
        for right in range(1,n):
            matrix[down][right] = matrix[down-1][right] + matrix[down][right-1]
    print(matrix)
    return matrix[m-1][n-1]

uniquePaths(3,7)
uniquePaths(3,2)