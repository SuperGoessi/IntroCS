#include <iostream>
#include <limits>

using namespace std;

int main()
{
    cout << "Hello world!" << endl;

    std::cin.clear();
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    std::cin.get();

    return 0;
}
