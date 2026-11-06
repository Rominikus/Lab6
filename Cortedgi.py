students = [
    ("Иван", 25, 4.5),
    ("Мария", 22, 4.8),
    ("Пётр", 30, 4.2),
    ("Анна", 20, 4.9)
]

# Самый старший
oldest = max(students, key=lambda s: s[1])
print(f"Самый старший: {oldest[0]}, {oldest[1]} лет")

# С самым высоким баллом
best = max(students, key=lambda s: s[2])
print(f"Лучший студент: {best[0]}, балл {best[2]}")

# Средний возраст
avg_age = sum(s[1] for s in students) / len(students)
print(f"Средний возраст: {avg_age:.1f}")

# Сортировка по баллу (убывание)
sorted_students = sorted(students, key=lambda s: s[2], reverse=True)
print("\nПо баллу:")
for name, age, gpa in sorted_students:
    print(f"{name}: {gpa}")