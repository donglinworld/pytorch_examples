#include <iostream>

extern "C" {
    int add_numbers(int a, int b) {
        std::cout << "enter c++ function";
        return a + b;
    }
}
