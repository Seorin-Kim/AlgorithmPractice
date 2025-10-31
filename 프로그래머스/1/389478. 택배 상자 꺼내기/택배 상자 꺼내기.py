def solution(n, w, num):
    h = n // w + 1
    board = [[0] * w for _ in range(h)]
    row = 1
    k = 1
    for i in range(h - 1, -1, -1):
        if k > n: break
        
        if row % 2 == 1:
            for j in range(w):
                board[i][j] = k
                k += 1
                if k > n: break
            row += 1
        else:
            for j in range(w - 1, -1, -1):
                board[i][j] = k
                k += 1
                if k > n: break
            row += 1
        
    for i in range(h):
        for j in range(w):
            if board[i][j] == num:
                if board[0][j] == 0:
                    return i
                else:
                    return i + 1
    