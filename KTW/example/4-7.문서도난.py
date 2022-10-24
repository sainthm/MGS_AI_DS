def getTime(time):
    H, M = time.split(":")
    return int(H) * 60 + int(M)

def solution(reports, times):
    answer = []
    tmp = []
    for report in reports:
        name, time = report.split()
        tmp.append([name, getTime(time)])
    
    # tmp.sort(key = lambda x : x[1])
    start, end = times.split()
    start = getTime(start)
    end = getTime(end)
    
    for name, minute in tmp:
        if start <= minute <= end:
            answer.append(name)
        # if minute > end:
        #     break
    
    return sorted(answer)

print(solution(["john 15:23", "daniel 09:30", "tom 07:23", "park 09:59", "luis 08:57"], "08:33 09:45"))
print(solution(["ami 12:56", "daniel 15:00", "luis 08:57", "bill 17:35", "bob 19:59", "tom 07:23", "john 15:23", "park 09:59"], "15:01 19:59"))



# def solution(reports, times) : 
#     sus_name = [i.split()[0] for i in reports]
#     sus_time = [i.split()[1] for i in reports]
    
#     investigate = times.split()
#     start = investigate[0]
#     end = investigate[1]
#     #print(sus_name, sus_time, start, end)
#     suspect = []
#     for i in range(len(sus_time)) :
#         if start <= sus_time[i] <= end : 
#             suspect.append(i)

#     def find_name(x) : 
#         return sus_name[x]
    
#     result = list(map(find_name, suspect))
#     return result

# HH:MM 을 변환하는 함수
# def getMinute(time):
#         hour = int(time.split(":")[0])
#         minute = int(time.split(":")[1])
#         return hour * 60 + minute
    
# def getMinute(time):
#     h, m = map(int, time.split(':'))
#     return h * 60 + m

# def getMinute(time):
#     h, m = time.split(':')
#     return int(h) * 60 + int(m)