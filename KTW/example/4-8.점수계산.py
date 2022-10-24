def solution(nums):
    answer = 0
    score = 0
    for x in nums:
        if x == 1:
            score += 1
            answer += score
        else:
            score = 0
    return answer

print(solution([1, 0, 1, 1, 1, 0, 0, 1, 1, 0]))