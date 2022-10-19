# s.find(s[i]) == i

def solution(s):
    answer = ""
    for i in range(len(s)):
        # print(s[i])
        if s.find(s[i]) == i:
            answer += s[i]
    
    return answer

print(solution("kkkkdsdfesdfaqqq"))