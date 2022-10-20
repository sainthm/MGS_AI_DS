# nums=[2, 5, 3, 1, 4]
# 1. 오름차순 정렬 : nums.sort() : 한 자리 숫자만 정렬이 제대로 됩니다.
# 2. 내림차순 정렬 : nums.sort(reverse = True)
# 3. 좌표정렬하기

# 1) [x, y]에서 x값에 의한 오름차순 정렬
def solution(nums):
    nums.sort(key = lambda v : (v[0]))
    return nums;

print(solution([[2, 3], [1, 4], [3, 1], [1, 2]]));

# 2) [x, y]에서 y값에 의한 오름차순 정렬 
def solution(nums):
    nums.sort(key = lambda v : (v[1]))
    return nums;

print(solution([[2, 3], [1, 4], [3, 1], [1, 2]]));

# 3) [x, y]에서 x값에 의한 내림차순 정렬
def solution(nums):
    nums.sort(key = lambda v : (-v[0]))
    return nums;

print(solution([[2, 3], [1, 4], [3, 1], [1 ,2]]));

# 4) [x, y]에서 y값에 의한 오름차순을 하되 y값이 같은 경우는 x값에 따라 오름차순한다.
def solution(nums):
    nums.sort(key = lambda v : (v[1], v[0]))
    return nums;

print(solution([[2, 3], [1, 4], [3, 1], [1, 1]]));