# Задание 3
# n = int(input("Введите целое число: "))

# for i in range(n + 1):
#     x = n - i
#     print(f"{n} = {i} + {x}")

# # Задание 6
def push(stack, item):
    """Добавляет элемент в конец списка (на вершину стека)."""
    stack.append(item)
    print(f"Push: {item} -> стек: {stack}")


def pop(stack):
    """Удаляет и возвращает элемент с вершины стека."""
    if len(stack) == 0:
        print("Ошибка: стек пуст!")
        return None
    item = stack.pop()
    print(f"Pop:  {item} <- стек: {stack}")
    return item


# --- Демонстрация работы стека ---
stack = []
print("=== Работа со стеком ===\n")

push(stack, 10)
push(stack, 20)
push(stack, 30)

print()
pop(stack)
pop(stack)
pop(stack)
pop(stack)  # проверка пустого стека