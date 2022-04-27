import sys
import itertools

# sys.stdin = open("07_input.txt", "r")
#
# n, m = map(int, sys.stdin.readline().split())
# map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# https://kimjingo.tistory.com/51
import itertools, sys

N, M = map(int, input().split(' ')) # 도시 크기 N, 치킨 집 개수 M
map = [list(map(int, input().split(' '))) for _ in range(N)] # 도시정보

BLANK = 0
HOUSE = 1
CHICKEN = 2

chicken_list = [(i, j) for i in range(len(map)) for j in range(len(map[i])) if map[i][j] == CHICKEN]
house_list = [(i, j) for i in range(len(map)) for j in range(len(map[i])) if map[i][j] == HOUSE]

def get_chicken_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


result = sys.maxsize

combination = list(itertools.combinations(chicken_list, M))
for c in combination:
    city_dist = 0
    for house in house_list:
        min_d = min([get_chicken_distance(picked,house) for picked in c])
        city_dist += min_d
    if city_dist < result:
        result = city_dist

print(result)