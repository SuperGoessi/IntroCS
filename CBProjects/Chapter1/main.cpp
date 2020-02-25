#include <iostream>

using namespace std;

//void doNothing(const int &x){
//}

int main()
{
//    int x;
//    doNothing(x);
//    std::cout << x;

//    int inputByUser {};
//    std::cout << "Enter an integer: ";
//    std::cin >> inputByUser;
//    std::cout << "Double that number is: " <<inputByUser * 2;

//    int input {};
//    std::cout << "Enter an integer: ";
//    std::cin >>input;
//    std::cout << "Double " << input << " is: " << input * 2 << std::endl;
//    std::cout << "Triple " << input << " is: " << input * 3 << std::endl;

    int firstNum {};
    int secondNum {};

    std::cout << "Enter an integer: ";
    std::cin >> firstNum;
    std::cout << "Enter another integer: ";
    std::cin >> secondNum;
    std::cout << firstNum << " + " << secondNum << " is " << firstNum + secondNum << "." << std::endl;
    std::cout << firstNum << " - " << secondNum << " is " << firstNum - secondNum << "." << std::endl;

    return 0;
}
