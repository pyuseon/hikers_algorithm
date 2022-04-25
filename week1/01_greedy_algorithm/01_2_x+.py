target_list = list(map(int, list(input())))
print(target_list)

result = target_list[0]
for i in target_list[1:]:
    if i == 0 or i == 1 or result == 0 or result == 1:
        result += i
    else:
        result *= i

print(result)