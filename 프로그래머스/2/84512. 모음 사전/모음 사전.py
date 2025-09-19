def solution(word):
    moeums = ['A', 'E', 'I', 'O', 'U']

    answer = len(word)
    for i in range(len(word)):
        tmp = 0
        for j in range(4-i, -1, -1):
            tmp += 5 ** j
        answer += tmp * moeums.index(word[i])
        
    return answer