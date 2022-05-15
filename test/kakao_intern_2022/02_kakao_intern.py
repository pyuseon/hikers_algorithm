from collections import deque
from itertools import combinations

queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]



def solution(queue1, queue2):
    half = int((sum(queue1) + sum(queue2)) / 2)

    # queue 두개를 2로 나눈 나머지가 0이 아니면 두 큐의 합의 맞출 수 없다.
    if (sum(queue1) + sum(queue2)) % 2 != 0:
        return -1

    deque1 = deque(queue1)
    deque2 = deque(queue2)

    answer = 0
    print(half)

    while sum(deque1) != sum(deque2):
        left_num = half - sum(deque1)
        deque1_first = deque1.popleft()
        deque2_first = deque2.popleft()
        print("****")
        print(left_num)

        if left_num < deque2_first:
            deque2.appendleft(deque2_first)
            deque2.append(deque1_first)
        elif left_num == 0:
            print("____________")
            print(left_num)
            answer += 1
            break
        else:
            deque1.appendleft(deque1_first)
            deque1.append(deque2_first)

        if len(deque1) == 0 or len(deque2) == 0 or answer > (len(queue1 + queue2) + 1):
            return -1

        answer += 1

    return answer


print(solution(queue1, queue2))
