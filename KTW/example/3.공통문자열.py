def solution(s):
    answer = ""
    for i in range(len(s[0])):
        common = set()
        for word in s:
            common.add(word[i])
        if len(common) == 1:
            answer += s[0][i]
            # answer += word[i]
        else:
            break
            
    return answer

print(solution(["long", "longtime", "longest"]))
print(solution(["lengi", "lengi", "lenti"]))
print(solution(["test", "tesking", "testing"]))