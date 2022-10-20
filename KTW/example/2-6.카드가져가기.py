def solution(nums, k):
    answer = 0
    n = len(nums)
    nums.sort(reverse = True)
    diff = []
    for i in range(1, n, 2):
        answer += nums[i]
        diff.append(nums[i-1] - nums[i])
    
    diff.sort(reverse = True)
    for i in range(k):
        answer += diff[i]
        
    return answer

print(solution([7, 8, 5, 9, 3, 1, 3, 1, 1, 9], 2))
print(solution([8, 2, 12, 12, 12, 12, 2, 2], 2))