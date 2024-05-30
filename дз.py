def sum_mod(vector):
    return sum(abs(x) for x in vector)

def find_min_sum(matrix):
    min_sum = float('inf')
    min_sum_row = []
    for row in matrix:
        curr_sum = sum_mod(row)
        if curr_sum < min_sum:
            min_sum = curr_sum
            min_sum_row = row
    return min_sum_row

Чтение матрицы из файла
matrix = []
with open('matrix.txt', 'r') as file:
    for line in file:
        row = list(map(int, line.strip().split()))
        matrix.append(row)

Нахождение строки с минимальной суммой модулей
result_row = find_min_sum(matrix)

Вывод элементов этой строки
print("Строка с минимальной суммой модулей элементов:", result_row)
