# 코테 진행 시, itertools 은 못씀
import collections

def solution(s):
    answer = ""
    sH = collections.Counter(s)
    maxC = 0
    # print(sH)
    for key, val in sH.items():
        # print(key, val)
        if val > maxC:
            maxC = val
            answer = key
    # print(maxC)
    
    return answer

print(solution("BACBACCACCBDEDE"))



# import collections 사용 불가할 경우

def solution_nocounter(s):
    answer = ""
    sH = collections.defaultdict(int)
    # print(sH['a'])
    for c in s:
        sH[c] += 1
    
    # print(sH)
    maxC = 0
    # print(sH)
    for key, val in sH.items():
        # print(key, val)
        if val > maxC:
                maxC = val
                answer = key
        # print(maxC)
    
    return answer

print(solution_nocounter("BACBACCACCBDEDE"))