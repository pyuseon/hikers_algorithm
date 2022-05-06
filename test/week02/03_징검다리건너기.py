# https://programmers.co.kr/learn/courses/30/lessons/64062
def solution(stones, k):
    answer = 0
    left = 1
    right = max(stones)

    while left <= right:
        zero_cnt = 0
        mid = (left + right) // 2

        for stone in stones :
            if stone - mid <= 0:
                zero_cnt += 1
            else:
                zero_cnt = 0

            if zero_cnt >= k :
                answer = mid
                break

        if zero_cnt < k :
            left = mid +1
        else:
            right = mid -1

    return answer