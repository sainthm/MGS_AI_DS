import collections
from curses.ascii import isupper
def solution(s, n):
    used = collections.defaultdict(int)
    s = "".join(s.split())
    for c in s:
        if c.isupper():
            used["shift"] = 1
            c = c.lower()
        used[c] = 1
    return len(used) <= n



# def solution_2(word, n):
#     myset = set(word.replace(" ", ""))
#     count = len(myset)
#     # print(count)
  
#     if count <= n:
#         return True
#     else:
#         return False


print(solution("time to time", 5))
print(solution("time to study", 7))
print(solution("Big Life is Good", 10))
print(solution("Life is Good", 7))

print(solution("Gab", 4))
# print(solution_2("Gab", 4))