list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Через множества
set1 = set(list1)
set2 = set(list2)

union = set1 | set2
intersection = set1 & set2
difference = set1 - set2

print(f"Объединение: {sorted(union)}")        # [1, 2, 3, 4, 5, 6, 7, 8]
print(f"Пересечение: {sorted(intersection)}")  # [4, 5]
print(f"Разность: {sorted(difference)}")       # [1, 2, 3]