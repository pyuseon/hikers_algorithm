import itertools as it

# https://stackoverflow.com/questions/38617330/split-string-into-chunks-of-same-letters
# https://pyquestions.com/how-do-i-use-itertools-groupby
s = input()

zero_to_one = 0
one_to_zero = 0
for k, g in it.groupby(s):
    if k == "0":
        zero_to_one += 1
    else:
        one_to_zero += 1
    # print(k, list(g))

print(min(zero_to_one, one_to_zero))