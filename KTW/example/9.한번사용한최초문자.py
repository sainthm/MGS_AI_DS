import collections

def solution(s):
    answer = -1
    sH = collections.Counter(s)
    for i in range(len(s)):
        if sH[s[i]] == 1:
             return i + 1

    return answer

print(solution("stringshowtime"))