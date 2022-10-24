def solution(nums, m):
    answer = 0
    sumN = 0
    left = 0
    for right in range(len(nums)):
        sumN += nums[right]
        while sumN > m:
            sumN -= nums[left]
            left += 1
        if sumN == m:
            answer += 1
    
    return answer

print(solution([1, 1, 2, 1, 3, 1, 1, 1, 1, 2], 6))
print(solution([1, 1, 1, 1, 1, 1, 3], 3))
print(solution([1, 2, 1, 2, 1, 2, 1], 3))