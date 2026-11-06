def quicksort(arr):
    """Быстрая сортировка - выбираем опорный элемент и разделяем список."""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # опорный элемент - середина
    
    left = [x for x in arr if x < pivot]      # меньше опорного
    middle = [x for x in arr if x == pivot]   # равные опорному
    right = [x for x in arr if x > pivot]     # больше опорного
    
    return quicksort(left) + middle + quicksort(right)

# Интерактивная часть
print("=== Быстрая сортировка ===")
numbers = input("Введите числа через пробел: ").split()
numbers = [int(x) for x in numbers]

print(f"\nИсходный список: {numbers}")
sorted_list = quicksort(numbers)
print(f"Отсортированный: {sorted_list}")