def solution(meeting):
    et = 0
    answer = 0
    meeting.sort(key = lambda v : (v[1], v[0]))
    # print(meeting)
    for x in meeting:
        if x[0] >= et:
            et = x[1]
            answer += 1
    
    return answer

print(solution([[1, 4], [2, 3], [3, 5], [4, 6], [5, 7]]))
print(solution([[3, 3], [1, 3], [2, 3]]))