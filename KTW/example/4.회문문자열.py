def solution(s):
    answer = "YES"
    s = s.upper()
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return "NO" # return 은 함수값을 반환하면서 *종료* 하는 역할까지함!!
        else:
            left += 1
            right -= 1
    
    return answer

print(solution("steets"))
print(solution("abcdseba"))