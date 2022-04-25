import heapq

# def solution(food_times, k):
#     if sum(food_times) <= k:
#         return -1
#
#     q = []
#     for i in range(len(food_times)):
#         heapq.heappush(q, (food_times[i], i+1))
#
#     sum_value = 0
#     previous = 0
#     length = len(food_times)
#
#     while sum_value + ((q[0][0] - previous)*length) <= k:
#         now = heapq.heappop(q)[0]
#         sum_value += (now - previous) * length
#         length -= 1
#         previous = now
#
#     result = sorted(q, key=lambda x: x[1])
#
#     return result[(k - sum_value) % length][1]


# https://tiktaek.tistory.com/42
def solution(food_times, k):

    if sum(food_times) <= k:
        return -1

    food_len = len(food_times)
    if food_len > k:
        return k+1

    queue = []
    for i, f in enumerate(food_times):  # heapq 생성
        heapq.heappush(queue, [f, i])   # [음식양, 인덱스]

    sum_time = 0
    prev_time = 0
    print(queue)
    while k >= sum_time:
        min_time, idx = queue[0]
        sum_time += food_len * (min_time-prev_time)
        heapq.heappop(queue)
        food_len = len(queue)
        prev_time = min_time
        print(queue)
        print(sum_time)


    queue.sort(key=lambda k :k[1])
    print("최종 큐")
    print(queue)
    return queue[(k-sum_time) % food_len][1]




# food_times = [4, 2, 3, 6, 7, 1, 5, 8]
# k = 16

food_times = [3, 1, 2]
k = 5

result = solution(food_times, k)

# def solution(food_times, k):
#
#     food_order = 0
#     for i in range(k+1):
#
#         while True:
#             if food_times[food_order] == 0:
#                 food_order = (food_order+1) % len(food_times)
#
#             if food_times[food_order] != 0:
#                 food_times[food_order] -= 1
#                 break
#
#         food_order = (food_order + 1) % len(food_times)
#         print("while문 탈출 food_order"+str(food_order))
#         print(food_times)
#
#     return food_order


