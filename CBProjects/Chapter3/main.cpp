#include <iostream>


using namespace std;

int getValue() {
    std::cerr << "getValue() called\n";
    return 4;
}

int add(int x, int y) {
    std::cerr << "add() called (x=" << x << ", y=" << y << ")" << '\n';
    return x + y;
}

void printResult(int z) {
    std::cout << "The answer is: " << z << "\n";
}

//int getUserInput() {
//    std::cout << "Enter a number: ";
//    int x{};
//    std::cin >> x;
//    return x;
//}

int getUserInput() {
//    LOGO << "getUserInput() called";
    std::cout << "enter a number: ";
    int x;
    std::cin >> x;
    return x;
}

//void printValue(int value) {
//    std::cout << value << "\n";
//}

void printValue(int value) {
    std::cout << value;
}

void a() {
    std::cout << "a() called\n";
}

void b() {
    std::cout << "b() called\n";
    a();
}

int main()
{
//    std::cerr << "main() called\n";
//    std::cout << getValue();

//    int x{ getValue() };
//    std::cerr << "main::x = " << x << '\n';
//
//    int y{ getValue() };
//    std::cerr << "main::y = " << y << '\n';
//
//    int z{ add(x, 5) };
//    std::cerr << "main::z = " << z << '\n';
//
//    printResult(z);

//    plog::init(plog::debug, "Logfile.txt");
//    LOGO << "main() called";
//
//    int x = getUserInput();
//    std::cout << "You entered: " << x;
//
//    printValue(5);
//    printValue(6);
//    printValue(7);

//    int x{ 1 };
//    std::cout << x << " ";
//
//    x = x + 2;
//    std::cout << x << " ";
//
//    x = x + 3;
//    std::cout << x << " ";

    a();
    b();

    return 0;
}
