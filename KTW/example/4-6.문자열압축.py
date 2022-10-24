def solution(s):
    answer = ""
    cnt = 1
    s = s+" "
    n = len(s)
    for i in range(n-1):
        if s[i] == s[i + 1]:
            cnt += 1
        else:
            answer += s[i]
            if cnt > 1:
                answer+= str(cnt)
            cnt = 1
    return answer


import collections
def solution_2(word) :
    word_dic = collections.Counter(word)
    word_dic
    my_str = ""
    for key, val in word_dic.items() : 
        if val > 1 : 
            my_str += key
            my_str += str(val)
        else :
            my_str += key
            
    return my_str


print(solution('KKHSSSSSSSE'))
print(solution('AAAbCCCDD'))
print(solution_2('KKHSSSSSSSE'))
print(solution_2('AAAbCCCDD'))