def solution(nums, m):
    answer = 0
    left = 0
    right = len(nums) - 1
    nums.sort()
    while left <= right:
        if nums[left] + nums[right] <= m:
            answer += 1
            left += 1
            right -= 1
        else:
            answer += 1
            right -= 1
    
    return answer

print(solution([90, 50, 70, 100, 60], 140))
print(solution([86, 95, 107, 67, 38, 49, 116, 22, 78, 53], 150))