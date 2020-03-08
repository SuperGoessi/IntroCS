#include <iostream>
#include <cstdint>
#include <iomanip>

using namespace std;

void writeValue(int x) {
    std::cout << "The value of x is : " << x << '\n';
}

int getValue() {
    int x;
    std::cin >> x;
    return x;
}

bool isEqual(int x, int y) {
    return (x==y);
}

int main()
{
//    std::cout << "bool:\t\t" << sizeof(bool) << " bytes\n";
//    std::cout << "char:\t\t" << sizeof(char) << " bytes\n";
//    std::cout << "wchar_t:\t" << sizeof(wchar_t) << " bytes\n";
//    std::cout << "char16_t:\t" << sizeof(char16_t) << " bytes\n";
//    std::cout << "char32_t:\t" << sizeof(char32_t) << " bytes\n";
//    std::cout << "short:\t\t" << sizeof(short) << " bytes\n";
//    std::cout << "int:\t\t" << sizeof(int) << " bytes\n";
//    std::cout << "long:\t\t" << sizeof(long) << " bytes\n";
//    std::cout << "long long:\t" << sizeof(long long) << " bytes\n";
//    std::cout << "float:\t\t" << sizeof(float) << " bytes\n";
//    std::cout << "double:\t\t" << sizeof(double) << " bytes\n";
//    std::cout << "long double:\t" << sizeof(long double) << " bytes\n";
//
//    int x[];
//    std::cout << "x is " << sizeof(x) << " bytes\n";

//    unsigned short x[0];
//    std::cout << "x was: " << x << '\n';
//
//    x = -1;
//    std::cout << "x is now: " << x << '\n';
//
//    x = -2;
//    std::cout << "x is now: " << x << '\n';

//    std::int16_t i (5);
//    std::cout << i;

//    std::cout << 5.0 << '\n';
//    std::cout << 6.7f << '\n';
//    std::cout << 9876543.21 << '\n';
//
//    std::cout << 9.87654321f << '\n';
//    std::cout << 987.654321f << '\n';
//    std::cout << 987654.321f << '\n';
//    std::cout << 9876543.21f << '\n';
//    std::cout << 0.0000987654321f << '\n';

//    std::cout << std::setprecision(16);
//    std::cout << 3.333333333333333333333333333333333333333333333333333333333333333f << '\n';
//    std::cout << 3.333333333333333333333333333333333333333333333333333333333333333 << '\n';

//    float f { 123456789.0f };
//    std::cout << std::setprecision(9);
//    std::cout << f << '\n';

//    double d{0.1};
//    std::cout << d << '\n';
//    std::cout << std::setprecision(17);
//    std::cout << d << '\n';

//    std::cout << std::setprecision(17);
//    double d1(1.0);
//    std::cout << d1 << std::endl;
//
//    double d2(0.1 + 0.1 + 0.1+ 0.1+ 0.1+ 0.1+ 0.1+ 0.1+ 0.1+ 0.1);
//    std::cout << d2 << std::endl;

//    double zero {0.0};
//    double posinf {5.0 / zero};
//    std::cout << posinf << std::endl;
//
//    double neginf {-5.0 / zero};
//    std::cout << neginf << std::endl;
//
//    double nan { zero / zero };
//    std::cout << nan << std:: endl;

//    std::cout << true << std::endl;
//    std::cout << !true << std::endl;
//
//    bool b{false};
//    std::cout << b << std::endl;
//    std::cout << !b << std::endl;
//
//    std::cout << true << std::endl;
//    std::cout << false << std::endl;
//
//    std::cout << std::boolalpha;
//
//    std::cout << true << std::endl;
//    std::cout << false <<std::endl;

//    std::cout << std::boolalpha;
//
//    bool b1 = 4;
//    std::cout << b1 << '\n';
//
//    bool b2 = 0;
//    std::cout << b2 << '\n';
//    return 0;

//    bool b {};
//    std::cout << "Enter a boolean value: ";
//    std::cin >> b;
//    std::cout << "You entered: " << b;

//    std::cout << "Enter an integer: ";
//    int x{0};
//    std::cin >> x;
//
//    std::cout << "Enter another integer: ";
//    int y{0};
//    std::cin >> y;
//
//    std::cout <<std::boolalpha;
//
//    std::cout << x << " and " << y << " are equal? ";
//    std::cout << isEqual(x, y);

//    std::cout << "Enter an integer: ";
//    int x {};
//    std::cin >> x;
//
//    if (x>0)
//        std::cout << "The value is positive\n";
//    else if (x<0)
//        std::cout <<"The value is negative\n";
//    else
//        std::cout << "The value is zero\n";

//    char ch{'a'};
//    std::cout << ch << '\n';
//    std::cout << static_cast<int>(ch) << '\n';
//    std::cout << ch << '\n';

    std::cout << "Input a keyboard character: ";

    char ch{};
    std::cin >> ch;
    std::cout << ch << " has ASCII code " << static_cast<int>(ch) << '\n';

    return 0;
}
