
a = ("a", "b", "c")
b = ("가", "나", "다")


a1 = zip(a, b)

# print(a1)
# print(*a1)

result1, result2 = zip(*a1)


# print(result1)
# print(result2)

print(result1 == a)
print(result2 == b)