def solution(name):
    alpha_cnt = 0
    cursor_cnt = len(name) - 1
    
    for i, alpha in enumerate(name):
        # A-Z 선택
        cnt = int(ord(alpha)) - int(ord('A'))
        alpha_cnt += min(cnt, 26 - cnt)
        
        # 이후에 연속된 A 체크
        next_A = i + 1
        while next_A < len(name) and name[next_A] == 'A':
            next_A += 1
        
        # 1. 처음부터 끝까지 순행
        # 2. 연속 A의 시작까지 갔다가, 역행
        # 3. 연속 A의 끝까지 역행했다가, 순행
        cursor_cnt = min([cursor_cnt, 2*i + len(name) - next_A, i + 2*(len(name) - next_A)])
        
    return alpha_cnt + cursor_cnt
    