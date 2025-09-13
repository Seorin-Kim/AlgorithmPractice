def solution(begin, target, words):
    from collections import deque
    
    answer = 0
    visited = [0] * len(words)
    
    if target not in words:
        return 0
    
    def bfs(begin_word):
        q = deque()
        q.append([begin_word, 0])
        
        while q:
            cur, cnt = q.popleft()
            
            if cur == target:
                return cnt
            
            for i, word in enumerate(words):
                diff = 0
                for j in range(len(cur)):
                    if not visited[i] and cur[j] != word[j]:
                        diff += 1
                
                if diff == 1:
                    q.append([word, cnt+1])
                    visited[i] = 1
    
    answer = bfs(begin)
    
    return answer