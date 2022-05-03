def solution(files):

    file_list = []
    for f_idx, file in enumerate(files):
        split_idx = []

        for s_idx in range(len(file)):
            # 인덱스가 2 이거나, 마지막 인덱스에 도달할 경우 멈춘다.
            if len(split_idx)== 2 or s_idx +1 == len(file):
                break
            # 앞은 문자, 뒤는 숫자 혹은 앞은 숫자 뒤는 문자일 경우 인덱스를 저장한다.
            if file[s_idx].isdigit() != file[s_idx+1].isdigit() :
                split_idx.append(s_idx)

        # 대 소문자 구분을 없애기 위해 모두 대문자로 설정
        head = file[:split_idx[0] + 1].upper()

        # tail 없는 경우 예외처리
        split_len = len(split_idx)
        number = file[split_idx[0] + 1:] if split_len != 2 else file[split_idx[0] + 1 : split_idx[1] +1]
        tail = "" if split_len != 2 else file[split_idx[1]+1 :]


        # split 결과 반환
        split_result = [head, int(number), tail, file]
        file_list.append(split_result)

    # 정렬하기
    file_list.sort(key = lambda x :(x[0], x[1]))

    # 파일 명만 가져오기
    answer = [i[-1] for i in file_list]
    return answer

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))

