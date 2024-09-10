"""
Транспонирование матрицы
Тестовые данные:
input:
1 2 3
4 5 6
7 8 9
5 4 3
output:
1 4 7 5
2 5 8 4
3 6 9 3
"""

import sys

# считывание списка из входного потока
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]

lst_in = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [5, 4, 3]]

# здесь продолжайте программу (используйте список lst_in)
for row in [[n[i] for n in lst_in] for i in range(len(lst_in[0]))]:
    print(*row)
