def solution(s):
    answer = ""
    
    for x in s:
        # print(x) # 하나씩 다 출력
        if x.isupper():
            answer += x.lower()
        else:
            answer += x.upper()
    
    return answer

print(solution("StuDY"))