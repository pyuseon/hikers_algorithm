# https://programmers.co.kr/learn/courses/30/lessons/64064

from itertools import permutations

def check_id(user, ban):
    if len(user) != len(ban):
        return False
    else:
        for i in range(len(ban)):
            if ban[i] == "*":
                continue

            if ban[i] == user[i]:
                continue
            else:
                return False
                break
    return True


def solution(user_id, banned_id):
    answer = []
    for user_perm in list(permutations(user_id, len(banned_id))):
        count = 0
        for user, ban in zip(user_perm, banned_id):

            if check_id(user, ban):
                count += 1

        if count == len(banned_id):
            if set(user_perm) not in answer:
                answer.append(set(user_perm))
    return len(answer)

users = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banneds = ["fr*d*", "abc1**"]

print(solution(users, banneds))