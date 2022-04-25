def solution(food_times, k):

    food_order = 0
    for i in range(k+1): # k 번만큼 반복한다 (k가 5라면 0부터 5까지 여섯번)
    # food_order가 3이고 food times가 3이면 첫번째로 다시 넘어가야 한다.

        if food_order == len(food_times):
            food_order = 0

        # 해당 순서의 음식이 0일 경우에는 다음 순서로 넘어가는 코드
        while True:
            if food_times[food_order] == 0:
                food_order += 1

            if food_order == len(food_times):
                food_order = 0

            if food_times[food_order] != 0:
                food_times[food_order] -= 1
                food_order += 1
                break


    return food_order