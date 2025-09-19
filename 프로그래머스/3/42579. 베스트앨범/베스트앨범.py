def solution(genres, plays):
    hash = {}
    for i in range(len(genres)):
        if genres[i] not in hash.keys():
            hash[genres[i]] = [(i, plays[i])]
        else:
            hash[genres[i]].append((i, plays[i]))
    
    pop_genre = []
    for genre in hash.keys():
        hash[genre].sort(key=lambda x: (-x[1], x[0]))
        sum = 0
        for song in hash[genre]:
            sum += song[1]
        pop_genre.append((genre, sum))
    
    pop_genre.sort(key=lambda x: x[1], reverse=True)
    
    answer = []
    for genre, _ in pop_genre:
        answer.append(hash[genre][0][0])
        if len(hash[genre]) > 1:
            answer.append(hash[genre][1][0])

            
    return answer