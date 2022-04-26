# https://programmers.co.kr/learn/courses/30/lessons/60057
# https://blog.daum.net/sualchi/13720348


def solution(s):
    cnt = 1
    total_cnt = len(s)
    if total_cnt == 1:
        return 1

    for str_len in range(1, int(len(s)/2)+1):
        split_list = [s[i:i+str_len] for i in range(0, len(s), str_len)]
        tmp_cnt = 0
        print(split_list)

        for str_idx in range(len(split_list)):
            if (str_idx+1) == len(split_list):
                if split_list[str_idx-1] != split_list[str_idx]:
                    tmp_cnt += len(split_list[str_idx])
                    break
                elif split_list[str_idx - 1] == split_list[str_idx]:
                    tmp_cnt += (len(str(cnt)) + len(split_list[str_idx]))
                    break

            if split_list[str_idx] == split_list[str_idx +1]:
                cnt += 1
            else:
                if cnt == 1:
                    tmp_cnt += len(split_list[str_idx])
                else:
                    tmp_cnt += (len(str(cnt)) + len(split_list[str_idx]))
                cnt = 1

        if tmp_cnt < total_cnt:
            total_cnt = tmp_cnt

    return total_cnt

s = "abcabcabcabcdededededede"

print(solution(s))