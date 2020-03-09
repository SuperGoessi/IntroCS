#include <iostream>
#include <cmath>
#include <cstdint>
#include <algorithm>

using namespace std;

//std::int_fast64_t pow(int base, int exp) {
//    std::int_fast64 result{ 1 };
//    while(exp) {
//        if (exp & 1) {
//            result *= base;
//        }
//        exp >>= 1;
//        base *= base;
//    }
//}

bool approximatelyEqual(double a, double b, double epsilon) {
    return (std::abs(a-b) <= (std::max(std::abs(a), std::abs(b)) * epsilon));
}

bool approximatelyEqualAbsRel(double a, double b, double absEpsilon, double relEpsilon) {
    double diff{ std::abs(a-b)};
    if (diff <= absEpsilon)
        return true;

    return (diff <= (std::max(std::abs(a), std::abs(b)) * relEpsilon));
}

int main()
{
//    int x{7};
//    int y{4};
//
//    std::cout << "int / int = " << x / y << "\n";
//    std::cout << "double / int = " << static_cast<double>(x) / y << "\n";
//    std::cout << "int / double = " << x/static_cast<double>(y) << "\n";
//    std::cout << "double / double = " << static_cast<double>(x) / static_cast<double>(y) << "\n";

//    std::cout << "Enter a divisor: ";
//    int x{};
//    std::cin >> x;
//
//    std::cout << "12 / " << x << " - " << 12 / x << "\n";

//    std::cout << "Enter an integer: ";
//    int x{};
//    std::cin >> x;
//
//    std::cout << "Enter another integer: ";
//    int y{};
//    std::cin >> y;
//
//    std::cout << "The remainder is: " << x % y << "\n";
//
//    if ((x%y) == 0) {
//        std::cout << x << " is evenly divisible by " << y << "\n";
//    }
//    else {
//        std::cout << x << " is not evenly divisible by " << y << "\n";
//    }

//    std::cout << powint(7, 12);

//    int x {5};
//    int y = ++x;
//
//    std::cout << x << ' ' << y;

//    int x{5};
//    int y{5};
//    std::cout << x << " " << y << '\n';
//    std::cout << ++x << " " << --y << '\n';
//    std::cout << x << " " << y << '\n';
//    std::cout << x++ << " " << y-- << '\n';
//    std::cout << x << " " << y << '\n';

    double a{ 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1};

    std::cout << approximatelyEqual(a, 1.0, 1e-8) << '\n';
    std::cout << approximatelyEqual(a-1.0, 0.0, 1e-8) << '\n';
    std::cout << approximatelyEqualAbsRel(a-1.0, 0.0, 1e-12, 1e-8) << '\n';

    return 0;
}
