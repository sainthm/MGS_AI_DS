from collections import Counter
def solution(s):
    c1 = Counter(s)
    max_val = max(c1.values())
    l = []
    for i in "abc":
        l.append(max_val - c1[i])
    return l

print(solution("aaabc"))
print(solution("bcaaa"))
print(solution("aaabb"))