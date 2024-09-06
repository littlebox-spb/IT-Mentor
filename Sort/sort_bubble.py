"""
Сортировка пузырьком
Тестовые данные:
input: 4 5 2 0 6 3 -56 3 -1
output: -56 -1 0 2 3 3 4 5 6
"""

lst = list(map(int, input().split()))
for l in range(len(lst)):
    for i in range(len(lst) - 1 - l):
        if lst[i] > lst[i + 1]:
            lst[i + 1], lst[i] = lst[i], lst[i + 1]
print(*lst)
