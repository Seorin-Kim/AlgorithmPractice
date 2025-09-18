def solution(participant, completion):
    hash = {}
    for name in participant:
        if name not in hash.keys():
            hash[name] = 1
        else:
            hash[name] += 1
    
    for name in completion:
        if hash[name] == 1:
            hash.pop(name)
        else:
            hash[name] -= 1
    
    return list(hash.keys())[0]
