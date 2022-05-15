# https://programmers.co.kr/learn/courses/30/lessons/17677
import math
from copy import deepcopy


def solution(str1, str2):
    str_list1 = [str1[i:i+2].upper() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    str_list2 = [str2[i:i+2].upper() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]

    # 교집합
    str_temp = deepcopy(str_list1)
    str_inter = []

    for s in str_list2:
        if s in str_temp:
            str_temp.remove(s)
            str_inter.append(s)

    # 합집합
    str_temp2 = deepcopy(str_list1)
    str_union = deepcopy(str_list1)

    for s in str_list2:
        if s not in str_temp2:
            str_union.append(s)
        else:
            str_temp2.remove(s)


    if len(str_inter) == 0 and len(str_union) == 0:
        answer = 1 *65536
    else:
        answer = math.trunc((len(str_inter) / len(str_union)) * 65536)
    return answer

str1 = "aa1+aa2"
str2 = "AAAA12"

print(solution(str1, str2))