# https://programmers.co.kr/learn/courses/30/lessons/60057
# https://blog.daum.net/sualchi/13720348


def solution(s):
    cnt = 1
    total_cnt = len(s)
    if total_cnt == 1:
        return 1

    # 길이 수 만큼 돌아가면서 리스트 쪼개기
    for str_len in range(1, int(len(s)/2)+1):
        split_list = [s[i:i+str_len] for i in range(0, len(s), str_len)]
        # 길이 초기화

        tmp_cnt = ""

        print(split_list)
        for str_idx in range(len(split_list)):

            # 리스트 마지막 값
            if str_idx == len(split_list)-1:

                if cnt == 1:
                    tmp_cnt += split_list[str_idx]
                    break
                else:
                    tmp_cnt += (str(cnt) + split_list[str_idx])
                    break

            if split_list[str_idx] == split_list[str_idx +1]:
                cnt += 1
            else:
                if cnt == 1:
                    tmp_cnt += split_list[str_idx]
                else:
                    tmp_cnt += (str(cnt) + split_list[str_idx])
                cnt = 1

        # print(tmp_cnt)

        if len(tmp_cnt) < total_cnt:
            total_cnt = len(tmp_cnt)

    return total_cnt

s = "aaaaaaaaaaaabcd"

print(solution(s))