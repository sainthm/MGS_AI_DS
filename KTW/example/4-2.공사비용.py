# 일반적인 방식
def solution(cost, m):
    answer = 0
    sumN = 0
    left = 0
    
    for right in range(len(cost)):
        sumN += cost[right]
        while sumN > m:
            sumN -= cost[left]
            left += 1
        answer = max(answer, right-left+1)
    
    return answer


# length 활용 방식
def solution_2(cost, m):
    answer = 0
    sumN = 0
    left = 0
    length = 0
    
    for right in range(len(cost)):
        sumN += cost[right]
        length += 1
        while sumN > m:
            sumN -= cost[left]
            left += 1
            length -= 1
        answer = max(answer, length)
    
    return answer

print(solution([0, 150, 100, 0, 150, 0, 70, 140], 350))
print(solution([100, 200, 300, 400, 500, 100], 300))

print(solution_2([0, 150, 100, 0, 150, 0, 70, 140], 350))
print(solution_2([100, 200, 300, 400, 500, 100], 300))