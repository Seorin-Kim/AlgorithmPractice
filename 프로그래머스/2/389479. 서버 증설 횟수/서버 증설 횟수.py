def solution(players, m, k):
    servers = [0] * len(players)
    cnt = [0] * len(players)
    
    for i in range(len(players)):
        need = players[i] // m
        if need > servers[i]:
            cnt[i] = need - servers[i]
            for j in range(k):
                if i + j >= len(players):
                    break
                servers[i+j] += cnt[i]
                        
    return sum(cnt)