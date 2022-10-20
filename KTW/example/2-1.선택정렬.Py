# 보통 이중 포문 활용



def solution(nums):
    n = len(nums)
    for i in range(0, n - 1):
        minIndex = i
        for j in range(i+1, n):
            if nums[j] < nums[minIndex]:
                minIndex = j
        nums[i], nums[minIndex] = nums[minIndex], nums[i]
        # print(nums)
    return nums

nums = [2, 4, 5, 1, 3]


print(solution(nums))