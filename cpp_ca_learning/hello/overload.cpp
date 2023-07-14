#include <stdlib.h>
#include <iostream>

/*
 * In C++, function overloading allows multiple functions to have the same name as long as they differ in their parameters.
 * It enables functions to handle different types/numbers of inputs.
 */

/*
 * In order to differentiate overloaded functions, at least one of the following properties must be true:
 *
 *  1) Each function has different types of parameters.
 *  2) Each function has a different number of parameters.
 *  For example, the add() function in the previous example can be overloaded once more by adding an extra parameter:
 */

int add(int a, int b) {
  return a + b;
}

double add(double a, double b) {
  return a + b;
}

int add(int a, int b, int c) {
    return a + b + c;
}

int main() {
  std::cout << add(3, 2);     // Calls add(int, int)
  std::cout << "\n";
  std::cout << add(5.3, 1.4);     // Calls add(double, double)
  return 0;
}

