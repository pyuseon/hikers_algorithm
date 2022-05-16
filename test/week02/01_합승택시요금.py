# 합승 택시 요금
# https://programmers.co.kr/learn/courses/30/lessons/72413

def floyd(graph, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j] )


def solution(n, s, a, b, fares):
    s, a, b = s-1, a-1, b-1
    INF = int(1e9)

    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for r in range(n):
        graph[r][r] = 0

    for start, end, fee in fares :
        graph[start -1][end -1], graph[end -1][start -1] = fee, fee

    floyd(graph, n)

    answer = INF

    for k in range(n):
        answer = min(answer, graph[s][k] + graph[k][a] + graph[k][b])
    return answer