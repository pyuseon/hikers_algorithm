# https://programmers.co.kr/learn/courses/30/lessons/17678
# https://jennnn.tistory.com/80?category=984548

def solution(n, t, m, timetable):
    answer = 0
    mintable = []

    for time in timetable:
        hour, min = time.split(":")
        mintable.append(int(hour)*60 + int(min))

    mintable.sort()

    busTime = [9 * 60 + t * i for i in range(n)]  # 버스 시간

    i = 0  # 버스에 탈 크루의 인덱스
    for bt in busTime:  # 버스 도착 시간을 순회하면서
        cnt = 0  # 버스에 타는 크루 수
        while cnt < m and i < len(mintable) and mintable[i] <= bt:
            i += 1
            cnt += 1
        if cnt < m:  # 버스에 자리 남았으면 버스타임에 내가 타면 됨
            answer = bt
        else:  # 버스에 탈 자리 없으면 맨 마지막 크루보다 1분전에 도착
            answer = mintable[i - 1] - 1

    return str(answer // 60).zfill(2) + ":" + str(answer % 60).zfill(2)

n = 1
t = 1
m = 5
timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]

print(solution(n, t, m, timetable))