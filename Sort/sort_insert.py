"""
Сортировка выбором
Тестовые данные:
input: 8 11 -53 2 10 11
output: -53 2 8 10 11 11
"""

lst = list(map(int, input().split()))
for l in range(len(lst)):
    for i in range(l, len(lst)):
        if lst[i] < lst[l]:
            lst[l], lst[i] = lst[i], lst[l]
print(*lst)
