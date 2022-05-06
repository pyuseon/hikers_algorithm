
def solution(str_input):
    stack = []
    for s in str_input :
        if s == "(" or s =="{":
            stack.append(s)
        elif s == ")" or s == "}":
            if len(stack) == 0:
                return False

            if (stack[-1] == "(" and  s == ")") or (stack[-1] == "{" and  s == "}") :
                stack.pop()
            else:
                return False
    return True


test = "{{}(})()"
print(solution(test))