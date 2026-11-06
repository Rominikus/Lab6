def input_matrix(rows, cols, name):
    """Ввод матрицы с клавиатуры."""
    print(f"\nВведите матрицу {name} ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        while True:
            row = input(f"Строка {i+1} (через пробел): ").split()
            if len(row) != cols:
                print(f"Ошибка! Нужно ввести {cols} чисел. Попробуйте снова.")
            else:
                try:
                    matrix.append([int(x) for x in row])
                    break
                except ValueError:
                    print("Ошибка! Введите целые числа. Попробуйте снова.")
    return matrix

def print_matrix(matrix, name=""):
    """Красивый вывод матрицы."""
    if name:
        print(f"\n{name}:")
    for row in matrix:
        print("  ".join(f"{x:4}" for x in row))

def add_matrices(A, B):
    """Сложение матриц."""
    rows = len(A)
    cols = len(A[0])
    result = [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]
    return result

def subtract_matrices(A, B):
    """Вычитание матриц."""
    rows = len(A)
    cols = len(A[0])
    result = [[A[i][j] - B[i][j] for j in range(cols)] for i in range(rows)]
    return result

def multiply_matrices(A, B):
    """Умножение матриц."""
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    
    result = [[0] * cols_B for _ in range(rows_A)]
    
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

# Интерактивная часть
print("=== Матричные операции ===")

# Ввод размеров матрицы A
print("\n--- Матрица A ---")
rows_A = int(input("Количество строк матрицы A: "))
cols_A = int(input("Количество столбцов матрицы A: "))
A = input_matrix(rows_A, cols_A, "A")

# Ввод размеров матрицы B
print("\n--- Матрица B ---")
rows_B = int(input("Количество строк матрицы B: "))
cols_B = int(input("Количество столбцов матрицы B: "))
B = input_matrix(rows_B, cols_B, "B")

# Вывод матриц
print_matrix(A, "Матрица A")
print_matrix(B, "Матрица B")

print("\n=== Результаты ===")

# Сложение и вычитание (только если размеры совпадают)
if rows_A == rows_B and cols_A == cols_B:
    print_matrix(add_matrices(A, B), "A + B")
    print_matrix(subtract_matrices(A, B), "A - B")
else:
    print(f"\n⚠️  Сложение и вычитание невозможны!")
    print(f"   Матрица A: {rows_A}x{cols_A}")
    print(f"   Матрица B: {rows_B}x{cols_B}")
    print(f"   Для сложения/вычитания размеры должны совпадать.")

# Умножение (только если cols_A == rows_B)
if cols_A == rows_B:
    print_matrix(multiply_matrices(A, B), "A × B")
else:
    print(f"\n⚠️  Умножение невозможно!")
    print(f"   Количество столбцов A ({cols_A}) должно равняться количеству строк B ({rows_B}).")