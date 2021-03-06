from collections import deque
n, k = map(int, input().split())

graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스에대한 정보를 담는 리스트

graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # 바이러스의 종류, 시간, 위치x, 위치 y 삽입
            data.append((graph[i][j], 0, i, j))


# 정렬 이후에 큐로 옮기기 (낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

# 바이러스가 퍼져나갈 수 있는 4가지 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 너비 우선 탐색(BFS) 진행
while q: # while q를 한다면 g가 비어있지 않다면 반복 실행 된다.
    virus, s, x, y = q.popleft()
    # 정확히 s 초가 지나거나 q가 빌때까지 반복
    if s == target_s:
        break

    for i in range(4):
        nx = x +dx[i]
        ny = y +dy[i]
        # 해당 위치로 이동 할 수 있는 경우
        if 0 <= nx and nx < n and 0 <= ny and ny < n :
            # 아직 방문하지 않은 위치라면 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s+1, nx, ny))

print(graph[target_x-1][target_y-1])