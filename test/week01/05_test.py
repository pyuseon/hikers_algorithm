# https://programmers.co.kr/learn/courses/30/lessons/60057
# 문자열 압축
def solution(s):
    answer = len(s)
    if answer == 1:
        return 1

    # 길이 수 만큼 돌아가면서 리스트 쪼개기
    for window in range(1, int(len(s) / 2) + 1):
        split_list = [s[i:i + window] for i in range(0, len(s), window)]

        res = ""
        cnt = 1
        split_list = split_list + ['']
        for i in range(len(split_list)-1):
            if split_list[i] == split_list[i + 1]:
                cnt += 1
            else:
                res += split_list[i] if cnt == 1 else str(cnt) + split_list[i]
                cnt = 1

        # Update answer
        if len(res) < answer:
            answer = len(res)

    return answer


s = "abcabcabcabcdededededede"
solution(s)