def score_cal(survey_type, choice):
    sorted_type = ["RT", "CF", "JM", "AN"]

    if survey_type in sorted_type:
        score = 4 - choice
    else:
        score = choice - 4

    result = ["".join(sorted(survey_type)), score]
    return result


def solution(survey, choices):
    score_dict = {"RT": 0, "CF": 0,"JM": 0, "AN": 0}

    for i in range(len(survey)):
        survey_type = survey[i]
        choice = choices[i]

        cal_result = score_cal(survey_type, choice)

        print(cal_result)
        score_dict[cal_result[0]] += cal_result[1]

    answer = ''
    for key in list(score_dict.keys()):
        target_score = score_dict[key]
        if target_score >= 0:
            answer += key[0]
        else:
            answer += key[1]

    return answer


survey = ["TR", "RT", "TR"]
choices =  [7, 1, 3]
print(solution(survey, choices))