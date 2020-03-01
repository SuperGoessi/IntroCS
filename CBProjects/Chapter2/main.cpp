#include <iostream>
#include "add.h"
#include "square.h"
#include "geometry.h"
using namespace std;
#define PRINT_JOE
#define FOO 9
#define PRINT
//void doPrint()
//{
//    std::cout << "In doPrint()\n";
//}
//
//void doB()
//{
//    std::cout << "In doB()\n";
//}
//
//void doA()
//{
//    std::cout << "Starting doA()\n";
//    doB();
//    std::cout << "Ending doA()\n";
//}
//
////int getValueFromUser() {
////    std::cout << "Enter an integer: ";
////    int input{};
////    std::cin >> input;
////
////    return input;
////}
//
//int returnFive()
//{
//    return 5;
//}
//
//void returnNothing()
//{
//    std::cout << "Hi" << "\n";
//}
//
//int getValueFromUser()
//{
//    std::cout << "Enter an integer: ";
//    int input {};
//    std::cin >> input;
//
//    return input;
//}
//
//void printValue(int x)
//{
//    std::cout << x << '\n';
//}
//
//void printValues(int x, int y)
//{
//    std::cout << x << '\n';
//    std::cout << y << '\n';
//}
//
//int add(int x, int y)
//{
//    return x + y;
//}
//
//int multiply(int z, int w)
//{
//    return z * w;
//}
//
//void printDouble(int value)
//{
//    std::cout << value << " double is: " << value * 2 << '\n';
//}
//
//int doubleNumber(int n)
//{
//    return 2*n;
//}
//
//void doSomething()
//{
//    std::cout << "Hello\n";
//}
//
//int doMath(int first, int second, int third, int fourth);

int add(int x, int y);

int getInteger();

void doSomething();

int main()
{
//    std::cout << "Starting main()\n";
//    doPrint();
//    doPrint();
//    std::cout << "Ending main()\n";

//    std::cout << "Starting main()\n";
//    doA();
//    std::cout << "Ending main()\n";
//
//    return 0;
//    getValueFromUser();
//    int num{};
//    std::cout << num << " doubled is: " << num * 2 << '\n';

//    std::cout << returnFive() << '\n';
//    std::cout << returnFive() + 2 << '\n';
//
//    returnFive();
//
//    int num {getValueFromUser()};
//    std::cout << num << " double is: " << num * 2 << '\n';

//    returnNothing();
//    std::cout << returnNothing();

//    int x{getValueFromUser()};
//    int y{getValueFromUser()};
//
//    std::cout << x << " + " << y << " = " << x + y << '\n';

//    int num {getValueFromUser()};
//    std::cout << num << " doubled is: " << num * 2 << '\n';

//    doPrint();
//    printValue(6);
//    add(2, 3);

//    printValues(6, 7);
//
//    int num {getValueFromUser()};
//    printDouble(num);
//
//    printDouble(getValueFromUser());

//    std::cout << add(4, 5) << '\n';
//    std::cout << add(1+2, 3*4) << '\n';
//
//    int a{5};
//    std::cout << add(a, a) << '\n';
//
//    std::cout << add(1, multiply(2, 3)) << '\n';
//    std::cout <<add(1, add(2,3)) << '\n';

//    std::cout << doubleNumber(getValueFromUser()) << std::endl;

//    int x{ 0 };
//    doSomething();
//    std::cout << " The sum of 3 and 4 is: " << add(3, 4) << '\n';
//    return 0;

//    int x{getInteger()};
//    int y{getInteger()};
//
//    std::cout << x << " + " << y << " is " << x + y << "\n";
//    #ifdef PRINT_JOE
//        std::cout << "Joe\n";
//    #endif // PRINT_JOE
//
//    #ifndef PRINT_BOB
//        std::cout << "Bob\n";
//    #endif // PRINT_BOB
//
//    std::cout << "Joe\n";
//
//    #if 0
//        std::cout << "Bob\n";
//        std::cout << "Steve\n";
//    #endif // 0
//
//    #ifdef FOO
//        std:cout << FOO;
//    #endif // FOO
//
//
//    doSomething();

    std::cout << "The sum of 3 and 4 is " << add(3, 4) << '\n';
    return 0;

}

int doMath(int first, int second, int third, int fourth) {
    return first + second * third / fourth;
}
