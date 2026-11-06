matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Через zip
transposed = [list(row) for row in zip(*matrix)]

# Вывод
print("Исходная матрица:")
for row in matrix:
    print(row)

print("\nТранспонированная матрица:")
for row in transposed:
    print(row)