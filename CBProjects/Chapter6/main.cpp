//#include "circle.h"
//#include "growth.h"
//#include "add.h"
#include <iostream>
extern int g_x;
int value { 5 };

extern const int g_y;
extern constexpr int g_z {2};

void doSomething() {
//    g_x = 3;
//    std::cout << g_x << '\n';

    std::cout << g_y << '\n';
    std::cout << g_z << '\n';
}
using namespace std;
//using namespace foo;

//int doSomething(int x, int y);

namespace foo
{
//    namespace goo {
//        int add(int x, int y) {
//            return x + y;
//        }
//    }


}

void print() {
    std::cout << " there\n";
}

void too() {
//    void print() {
//        std::cout << "Hello";
//    }

    std::cout << "global variable value: " << value << '\n';
}

int main()
{
//    std::cout << foo::doSomething(4, 3) << '\n';

//    std::cout << basicMath::pi << '\n';
//    std::cout << basicMath::e << '\n';
//    std::cout << basicMath::add(4, 3) << '\n';

//    namespace boo = foo::goo;
//    std::cout << boo::add(3, 4) << '\n';

//    foo::print();
//    ::print();

//    doSomething();
//
//    std::cout << g_y << '\n';
//    std::cout << g_z << '\n';
//    std::cout << g_x << '\n';
//
//    g_x = 5;
//    std::cout << g_x << '\n';

//    int apples { 5 };
//
//    {
//        std::cout << apples << '\n';
//
//        int apples{ 0 };
//        apples = 10;
//
//        std::cout << apples << '\n';
//    }
//
//    std::cout << apples << '\n';

//    int value { 7 };
//    ++value;
//
//    --(::value);
//    std::cout << "local variable value: " << value << "\n";
//    too();

    std::cout << g_x;

    return 0;
}
