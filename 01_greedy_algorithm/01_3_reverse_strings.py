string = input()

zero_to_one = 0
one_to_zero = 0

if string[0] == "1":
    one_to_zero += 1
else:
    zero_to_one += 1

for i in range(1, len(string)):
    if string[i] != string[i-1]:
        if string[i] == "1":
            one_to_zero += 1
        else:
            zero_to_one += 1

print(min (one_to_zero, zero_to_one))
