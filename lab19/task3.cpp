#include <iostream>
using namespace std;

int factorial(int n) {
    if (n == 0) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

int main() {
    // Example test cases
    cout << "Factorial = " << factorial(5) << endl;  // Output: Factorial = 120
    cout << "Factorial = " << factorial(0) << endl;  // Output: Factorial = 1
    
    return 0;
}
