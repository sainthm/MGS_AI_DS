def solution(word) :
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