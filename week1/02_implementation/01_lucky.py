# https://www.acmicpc.net/problem/18406
# 123402
import time

start_time = time.time()
target_list = list(map(int, list(input())))
print(target_list)

half_len = int(len(target_list)/2)
first_sum = sum(target_list[:half_len])
last_sum = sum(target_list[half_len:])

if first_sum == last_sum:
    print("LUCKY")
else:
    print("READY")

print(time.time() - start_time)