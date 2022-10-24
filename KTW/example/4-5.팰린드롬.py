from collections import Counter
def solution(s):
    answer = 'true'
    c = Counter(s)
    cnt = 0
    for i in c.values():
        if i % 2 == 1:
            cnt+=1
        # if cnt > 1:
        #     return 'false'        
        
    return cnt <= 1

print(solution('abbac'))
print(solution('abcbbbe'))
print(solution('ccccc'))