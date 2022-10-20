def solution(nums) : 
    n = len(nums)
    answer = [ 0 for x in range(len(nums))]
    
    for i in range(n - 1):
        minIndex = i 
        for j in range(i + 1, n): 
            if nums[minIndex] > nums[j]: 
                minIndex = j
        
        if i != minIndex:
            nums[i], nums[minIndex] = nums[minIndex], nums[i]
            
            answer[i] += 1
            answer[minIndex] += 1
                
    return answer

print(solution([4, 2, 5, 1, 3]))