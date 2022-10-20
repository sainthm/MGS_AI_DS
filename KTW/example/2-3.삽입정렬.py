def solution(nums):
    n = len(nums)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
            else:
                break
        # print(nums)
    
    return nums

print(solution([5, 4, 2, 3, 1]))