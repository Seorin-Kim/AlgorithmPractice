def solution(info, n, m):
    dp = [1000] * m     # dp[b]: b_sum이 b일 때 가능한 최소 a_sum
    dp[0] = 0
    
    for a, b in info:
        new = [1000] * m
        
        # a_sum += a
        for j in range(m):
            if dp[j] != 1000:
                na = dp[j] + a
                if na < n and na < new[j]:
                    new[j] = na
        
        # b_sum += b
        for j in range(m):
            if dp[j] != 1000:
                nj = j + b
                if nj < m and dp[j] < new[nj]:
                    new[nj] = dp[j]
        
        dp = new
    
    if min(dp) != 1000:
        return min(dp)
    else:
        return -1
