#include <iostream>

void doSomething() {
    #ifdef PRINT
        std::cout << "Printing";
    #endif // PRINT
    #ifndef PRINT
        std::cout <<"Not printing";
    #endif // PRINT
}
