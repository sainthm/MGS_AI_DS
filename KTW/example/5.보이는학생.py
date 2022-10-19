# for - else 구문
# for 문이 돌면서 break 로 멈추면 else로 오지않음
# for 문이 자연스럽게 끝나면 else 문으로 내려옴
def solution(nums):
    answer = 1
    maxH = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > maxH:
            answer += 1
            maxH = nums[i]
    
    return answer

print(solution([130, 135, 148, 140, 145, 150, 150, 153]))