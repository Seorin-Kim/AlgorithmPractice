def solution(sizes):
    max_w, max_h = 0, 0
    for wallet in sizes:
        if wallet[0] < wallet[1]:
            wallet[0], wallet[1] = wallet[1], wallet[0]
        
        if wallet[0] > max_w:
            max_w = wallet[0]
        if wallet[1] > max_h:
            max_h = wallet[1]
    
    return max_w * max_h