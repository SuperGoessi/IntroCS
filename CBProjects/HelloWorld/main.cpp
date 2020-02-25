#include <iostream>
#include <limits>

using namespace std;

int main()
{
//    cout << "hello world!" << endl;
//
//    std::cin.clear();
//    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
//    std::cin.get();
//
//    int x{};

//    int x{5};
//    std::cout <<x;
//
//    std::cout << "Hello" << "World";
//
//    std::cout << " x is equal to: " << x << std::endl;
//
//    std::cout << "Hi!" << std::endl;
//    std::cout << "My name is Alex." << std::endl;
//
//    std::cout << "x is equal to: " << x << '\n';
//    std::cout << "And that's all, folks!\n";
//
//    return 0;

    std::cout << "Enter a number: ";
    int x{ };
    std::cin >> x;
    std::cout << "You entered " << x << '\n';
    return 0;

}
