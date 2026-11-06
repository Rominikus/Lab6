n = int(input("Введите размер массива: "))
arr =[]
for i in range(n):
    x = int(input(f"Введите элемент {i}: "))
    arr.append(x)
target=float(input('Введите число, которое ищете: '))
def binary_search(arr, target):
    """Ищет индекс элемента target в отсортированном массиве arr."""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # не найдено
print(f'Индекс искомого числа: {binary_search(arr, target)}')