# https://velog.io/@djagmlrhks3/Algorithm-BaekJoon-11053.-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-by-Python
# https://www.acmicpc.net/problem/18353
n = int(input())
array = list(map(int, input().split()))
array.reverse()

dp = [1]*n
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] +1)

print(n - max(dp))