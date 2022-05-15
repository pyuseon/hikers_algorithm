def rotate_rc(rc):
    top = 0
    bottom = len(rc) - 1

    left = 0
    right = len(rc[0]) -1

    while left < right and top < bottom:

        prev_value = rc[top+1][left]

        for i in range(left, right +1):
            current_value = rc[top][i]
            rc[top][i] = prev_value
            prev_value = current_value

        top += 1

        for i in range(top, bottom+1):
            current_value = rc[i][right]
            rc[i][right] = prev_value
            prev_value = current_value

        right -= 1

        for i in range(right, left-1, -1):
            current_value = rc[bottom][i]
            rc[bottom][i] = prev_value
            prev_value = current_value

        bottom -= 1

        for i in range(bottom, top-1, -1):
            current_value = rc[i][left]
            rc[i][left] = prev_value
            prev_value = current_value

        left += 1

    return rc

def shift_row(rc):
    return [rc[-1]] + rc[0:len(rc)-1]

def solution(rc, operations):
    answer = rc
    for operation in operations:
        if operation == "Rotate":
            answer = rotate_rc(answer)
        elif operation == "ShiftRow":
            answer = shift_row(answer)
    return answer

rc = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
operation = ["Rotate"]
print(solution(rc, operation))