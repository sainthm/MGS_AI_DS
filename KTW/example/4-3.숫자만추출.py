def solution(s):
    answer = ""
    for value in s:
        if 48 <= ord(value) <= 57:
            answer += value
    
    return int(answer)

print(solution("gOen2Ts8eSoft"))


# ASCII 코드를 모를 경우
def solution_2(s):
    answer = ""
    for value in s:
        if value.isdigit():
            answer += value
    
    return int(answer)

print(solution_2("gOen2Ts8eSoft"))