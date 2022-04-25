n, m = map(int, input().split())
weights = list(map(int, input().split()))

# 오름차순 정렬
weights.sort()

result = 0

for i in range(len(weights)):
    for j in weights[i+1:]:
        if weights[i] < j:
            result += 1

print(result)