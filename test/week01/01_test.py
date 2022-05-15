# 거리두기 확인하기
# https://programmers.co.kr/learn/courses/30/lessons/81302
# https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL2-%EA%B1%B0%EB%A6%AC%EB%91%90%EA%B8%B0-%ED%99%95%EC%9D%B8%ED%95%98%EA%B8%B0-Python
from collections import deque


def bfs(place):
    p_locations = []

    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                p_locations.append((i, j))

    if not p_locations:
        return True


    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for x, y in p_locations:
        queue = deque()
        queue.append((x, y))
        visited = [[False] * 5 for i in range(5)]
        distance = [[0] * 5 for i in range(5)]
        visited[x][y] = True

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    if place[nx][ny] == "O" and distance[nx][ny] <= 2:
                        queue.append((nx, ny))
                        distance[nx][ny] = distance[x][y] + 1
                    if place[nx][ny] == "P" and distance[x][y] <= 1:
                        return False

    return True


def solution(places):
    answer = []
    for place in places:
        print(bfs(place))
        if bfs(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))