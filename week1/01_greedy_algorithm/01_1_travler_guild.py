n = int(input())

travler = list(map(int, input().split()))

travler.sort()
print(travler)

result = 0
count = 0

for i in travler:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)
