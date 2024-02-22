def solution(n, results):
    answer = 0
    graph = [[int(1e9) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        graph[i][i] = -1
    for w, l in results:
        graph[w - 1][l - 1] = True
        graph[l - 1][w - 1] = False
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] == int(1e9) or i == j:
                    continue
                if graph[i][k] == graph[k][j]:
                    graph[i][j] = graph[i][k]
                    graph[j][i] = not graph[i][k]
    for i in range(n):
        if int(1e9) in graph[i]:
            continue
        answer += 1
    
    return answer