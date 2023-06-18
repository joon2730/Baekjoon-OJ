#include <iostream>

int fibonacci(int N) {
    if (N == 0) {
        return 0;
    } else if (N == 1) {
        return 1;
    } else {
        return fibonacci(N-1) + fibonacci(N-2);
    }
}

int main() {
    int n;
    std::cin >> n;
    std::cout << fibonacci(n);
}