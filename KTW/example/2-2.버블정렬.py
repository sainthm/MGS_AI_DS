# def solution(nums):
#     n = len(nums)
#     # for i in range(n - 1, 0, -1):
#     for i in range(n - 1):
#         # for j in range(i):
#         for j in range(n-i-1):
#             if nums[j] > nums[j + 1]:
#                 nums[j], nums[j + 1] = nums[j + 1], nums[j]
#         # print(nums)
    
#     return nums

# print(solution([5, 4, 2, 1, 3]))


def solution(nums):
    n = len(nums)
    for i in range(n - 1):
        for j in range(n-i-1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        # print(nums)
    
    return nums

print(solution([5, 4, 2, 1, 3]))