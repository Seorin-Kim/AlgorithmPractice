def solution(m, n, puddles):
    puds = [(i-1, j-1) for [i, j] in puddles]
    paths = [[0] * m for _ in range(n)]
    
    paths[0][0] = 1
    for j in range(n):
        for i in range(m):
            if (i, j) in puds:
                paths[j][i] = 0
                continue
            if i > 0:
                paths[j][i] = (paths[j][i] + paths[j][i-1]) % 1000000007
            if j > 0:
                paths[j][i] = (paths[j][i] + paths[j-1][i]) % 1000000007
    
    return paths[j][i]