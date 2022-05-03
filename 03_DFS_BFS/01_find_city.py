import sys
from collections import deque
sys.stdin = open("07_input.txt", "r")

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


# 모든 도시에 대한 최단거리 초기화
distance = [-1]*(n+1)
distance[x] = 0

# 너비 우선 탑색 BFS 수행
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동 할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            #최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)


    # 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
    check = False
    for i in range(1, n+1):
        if distance[i] == k:
            print(i)
            check = True

    # 만약 최단 거리가 K인 도시가 없다면, -1 출력
    if check == False:
        print(-1)