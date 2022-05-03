# 기둥 생성시 0
def col_make(x, y, result):
    # 바닥 위에 있거나
    botton_start = (y == 0)

    # 보의 한쪽 끝 부분 위에 있거나 (보의 양쪽에 다 있으면 안된다!)
    left_bo = [x - 1, y, 1]
    right_bo = [x, y, 1]

    bo_condition = (left_bo in result) or (right_bo in result)

    # 다른 기둥 위에 있거나
    botton_col = [x, y - 1, 0]
    col_condition = (botton_col in result)

    final_condition = botton_start or bo_condition or col_condition

    return final_condition


# 보 생성시 1
def bo_make(x, y, result):

    # 한쪽 끝에 기둥이 있는 경우 (둘중 하나만 충족)
    left_col = [x, y - 1, 0]
    right_col = [x + 1, y - 1, 0]
    col_conditon = (left_col in result) or (right_col in result)
    # 양쪽에 보가 있는 경우
    left_bo = [x - 1, y, 1]
    right_bo = [x + 1, y, 1]

    bo_conditon = (left_bo in result) and (right_bo in result)

    final_condition = col_conditon or bo_conditon
    return final_condition



def check_condtion(result):
    for x,y,stuff in result:
        if stuff == 0:
            if col_make(x, y, result):
                continue
            return False
        elif stuff == 1:
            if bo_make(x, y, result):
                continue
            return False
    return True


def solution(n, build_frame):
    result = []

    for target_build in build_frame:
        print(target_build)
        x, y, stuff, operation = target_build
        if operation == 0:
            result.remove([x, y, stuff])
            if check_condtion(result) == False:
                result.append([x, y, stuff])
        else:
            result.append([x, y, stuff])
            if check_condtion(result) == False:
                result.remove([x, y, stuff])

    return sorted(result)


build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
n = 5

print(solution(n, build_frame))
