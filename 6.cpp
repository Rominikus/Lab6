// Лабораторная работа №6, Вариант 6
// Задание 3 и Задание 6 (стек на списке)

#include <iostream>
#include <vector>
#include <optional>   // для std::optional (C++17)

// --- Задание 6: стек на std::vector ---

// Добавляет элемент в конец вектора (на вершину стека)
void push(std::vector<int>& stack, int item) {
    stack.push_back(item);
    std::cout << "Push: " << item << " -> стек: [ ";
    for (int x : stack) std::cout << x << " ";
    std::cout << "]\n";
}

// Удаляет и возвращает элемент с вершины стека.
// Если стек пуст — возвращает std::nullopt (аналог None в Python).
std::optional<int> pop(std::vector<int>& stack) {
    if (stack.empty()) {
        std::cout << "Ошибка: стек пуст!\n";
        return std::nullopt;
    }
    int item = stack.back();
    stack.pop_back();
    std::cout << "Pop:  " << item << " <- стек: [ ";
    for (int x : stack) std::cout << x << " ";
    std::cout << "]\n";
    return item;
}

int main() {
    setlocale(LANG_RU, "Russian");

    // --- Задание 3 ---
    int n;
    std::cout << "Введите целое число: ";
    std::cin >> n;

    for (int i = 0; i <= n; ++i) {
        int x = n - i;
        std::cout << n << " = " << i << " + " << x << "\n";
    }

    std::cout << "\n";

//     // --- Задание 6: демонстрация работы стека ---
//     std::vector<int> stack;
//     std::cout << "=== Работа со стеком ===\n\n";

//     push(stack, 10);
//     push(stack, 20);
//     push(stack, 30);

//     std::cout << "\n";
//     pop(stack);
//     pop(stack);
//     pop(stack);
//     pop(stack);  // проверка пустого стека

//     return 0;
// }