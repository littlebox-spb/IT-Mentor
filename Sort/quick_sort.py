def quick_sort(s):
    A = []
    B = []
    D = []
    if len(s) <= 1:
        return s
    mid = s[0]
    for i in range(len(s)):
        if s[i] < mid:
            A.append(s[i])
        elif s[i] == mid:
            D.append(s[i])
        else:
            B.append(s[i])
    return quick_sort(A) + D + quick_sort(B)


print(quick_sort([19, 4, 5, 17, 1]))
assert quick_sort([19, 4, 5, 17, 1]) == [1, 4, 5, 17, 19]

print(quick_sort([16, 19, 2, 12, 20, 15, 20, 15]))
assert quick_sort([16, 19, 2, 12, 20, 15, 20, 15]) == [2, 12, 15, 15, 16, 19, 20, 20]

print(quick_sort([12, 13, 13, 1, 13, 3, 19, 8, 4]))
assert quick_sort([12, 13, 13, 1, 13, 3, 19, 8, 4]) == [1, 3, 4, 8, 12, 13, 13, 13, 19]

print("Все проверки пройдены!")
