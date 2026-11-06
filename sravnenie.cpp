#include <iostream>
#include <vector>

int main() {
    std::vector<int> numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int result = 0;
    
    for (int x : numbers) {
        if (x % 2 == 0) {
            result += x * x;
        }
    }
    
    std::cout << "Результат: " << result << "\n";
    return 0;
}