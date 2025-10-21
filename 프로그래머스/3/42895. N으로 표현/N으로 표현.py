def solution(N, number):
    ary = []
    
    for cnt in range(1, 9):
        tmp = set()
        tmp.add(int(str(N) * cnt))
        
        for i in range(cnt - 1):
            for op1 in ary[i]:
                for op2 in ary[-i - 1]:
                    tmp.add(op1 + op2)
                    tmp.add(op1 * op2)
                    tmp.add(op1 - op2)
                    if op2 != 0:
                        tmp.add(op1 // op2)
        
        if number in tmp:
            return cnt
        ary.append(tmp)
            
    return -1