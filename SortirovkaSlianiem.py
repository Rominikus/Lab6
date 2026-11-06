def merge_sort(arr):
    """Сортировка слиянием - рекурсивный алгоритм."""
    if len(arr) <= 1:
        return arr
    
    # Разделяем список пополам
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Сливаем две отсортированные половины
    return merge(left, right)

def merge(left, right):
    """Слияние двух отсортированных списков."""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Добавляем оставшиеся элементы
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Интерактивная часть
print("=== Сортировка слиянием ===")
numbers = input("Введите числа через пробел: ").split()
numbers = [int(x) for x in numbers]

print(f"\nИсходный список: {numbers}")
sorted_list = merge_sort(numbers)
print(f"Отсортированный: {sorted_list}")