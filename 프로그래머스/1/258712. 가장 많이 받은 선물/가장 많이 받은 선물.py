def solution(friends, gifts):
    name_idx = {name: i for i, name in enumerate(friends)}
    board = [[0] * len(friends) for _ in range(len(friends))]
    for rec in gifts:
        giver, taker = rec.split()
        board[name_idx[giver]][name_idx[taker]] += 1
        
    gift_idx = []
    for i in range(len(friends)):
        give = sum(board[i])
        take = 0
        for j in range(len(friends)):
            take += board[j][i]
        gift_idx.append(give - take)
    
    results = [0] * len(friends)
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            if board[i][j] > board[j][i]:
                results[i] += 1
            elif board[i][j] < board[j][i]:
                results[j] += 1
            else:
                if gift_idx[i] > gift_idx[j]:
                    results[i] += 1
                elif gift_idx[i] < gift_idx[j]:
                    results[j] += 1
    
    return max(results)