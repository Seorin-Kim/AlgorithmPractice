def solution(edges):
    graph = {}
    for src, dst in edges:
        # graph[vertex] : [나가는 edge 개수, 들어오는 edge 개수]
        if src not in graph.keys():
            graph[src] = [0, 0]
        if dst not in graph.keys():
            graph[dst] = [0, 0]
        graph[src][0] += 1
        graph[dst][1] += 1

    answer = [0] * 4
    for v in graph.keys():
        # 생성한 정점 : 나가는 edge 2개 이상 + 들어오는 edge 0개
        if graph[v][0] >= 2 and graph[v][1] == 0:
            answer[0] = v
        # 막대 그래프 : 나가는 edge 0개 + 들어오는 edge 1개 이상 (막대모양 그래프의 가장 끝 vertex 기준으로 개수 세기)
        elif graph[v][0] == 0 and graph[v][1] >= 1:
            answer[2] += 1
        # 8자 그래프 : 나가는 edge 2개 + 들어오는 edge 2개 이상 (8자 그래프의 중심 vertex 기준으로 개수 세기)
        elif graph[v][0] == 2 and graph[v][1] >= 2:
            answer[3] += 1
        # 도넛 그래프 : 생성한 정점에서 나가는 edge 개수 - 막대/8자 그래프 개수
    answer[1] = graph[answer[0]][0] - answer[2] - answer[3]
        
    return answer