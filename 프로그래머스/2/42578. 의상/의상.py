def solution(clothes):
    hash = {}
    for item in clothes:
        if item[1] not in hash.keys():
            hash[item[1]] = [item[0]]
            pass
        else:
            hash[item[1]].append(item[0])
    print(hash)
    
    answer = 1
    for k in hash.keys():
        answer *= (len(hash[k]) + 1)
    
    return answer - 1