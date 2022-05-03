# https://programmers.co.kr/learn/courses/30/lessons/60058
# https://jiwon-lee-it.tistory.com/44

def is_balansed(string):
    cnt = 0

    for s in string:
        if s == "(":
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= -1
    return True


def split_string(string):
    cnt = 0
    for i, s in enumerate(string):
        if s == "(":
            cnt += 1
        else:
            cnt -= 1

        if cnt == 0:
            u = string[:i + 1]
            v = string[i + 1:]
            return u, v


def solution(p):
    answer = ''
    if p == '':
        return answer

    u, v = split_string(p)
    print(u)
    print(v)

    if is_balansed(u):
        answer = u + solution(v)
    else:
        answer += "("
        answer += solution(v) #""
        answer += ")"

        u = list(u[1:-1])

        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('

        answer += "".join(u)

    return answer


p = "(()())))(("
print(solution(p))