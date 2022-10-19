import collections

def solution(nums):
    answer = -1
    m = max(nums)
    nH = collections.Counter(nums)
    for i in range(m, 0, -1):
        if nH[i] == 1:
             return i

    return answer

print(solution([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 7]))