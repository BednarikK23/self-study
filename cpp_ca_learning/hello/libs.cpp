#include <stdlib.h>
#include <cmath>
#include <iostream>
#include <string>

// Další standartní knihovny:
/*
 *  <vector>: This library provides a dynamic array implementation called std::vector.
 * It allows you to create resizable arrays and provides various member functions for accessing, modifying, and manipulating the elements.

 *  <algorithm>: This library provides a collection of algorithms for performing common operations on containers, such as sorting, searching, and transforming elements.
 *  It includes functions like std::sort(), std::find(), std::transform(), and many more.

 *  <array>: The <array> library provides a fixed-size array container called std::array.
 *  It allows you to create arrays with a compile-time fixed size and provides similar functionalities to std::vector, but with a fixed size.

 *  <map> and <unordered_map>: These libraries provide associative container implementations for key-value pairs.
 *  The <map> library implements a balanced binary search tree-based map, while <unordered_map> implements a hash table-based map.
 *  They allow efficient lookups and retrieval of values based on keys.

 *  <set> and <unordered_set>: These libraries provide implementations of sets, which are containers that store unique elements.
 *  Similar to maps, <set> uses a balanced binary search tree, while <unordered_set> uses a hash table for efficient element retrieval.

 *  <queue>, <stack>, and <deque>: These libraries provide implementations of queue, stack, and deque (double-ended queue) data structures, respectively.
 *  They offer various member functions for inserting, accessing, and removing elements from these containers
 */


int main() {

  // cmath
  // 1) Trigonometric functions: sin, cos, tan, asin, acos, atan.
  // 2) Exponential and logarithmic functions: exp, log, log10, pow, sqrt.
  // 3) Rounding and absolute value functions: ceil, floor, abs.
  // 4) Other mathematical functions: fmod, fabs, fmin, fmax.

  double x = 2.5;
  double y = 1.3;

  double result1 = std::sin(x);
  // in c++ ^ is bitwise XOR operator, for exponentiation use pow() function
  double result2 = std::pow(x, y);
  double result3 = std::fabs(-3.7);

  std::cout << "sin(" << x << ") = " << result1 << std::endl;
  std::cout << x << " ^ " << y << " = " << result2 << std::endl;
  std::cout << "|-3.7| = " << result3 << std::endl;

  // string
  // 1) String manipulation functions: length, substr, find, replace, append.
  // 2) String comparison functions: compare, ==, !=, <, >.
  //    -> 3 ways to compare strings: a) strcmp() (- C library <string.h>) b) == c) compare() (- c++ library <string>)
  // 3) Conversion functions: stoi, stod, to_string.
  // 4) Character manipulation functions: toupper, tolower.
  std::string str1 = "Hello";
  std::string str2 = "World";

  // String manipulation
  std::string combined = str1 + " " + str2;
  std::cout << "Combined string: " << combined << std::endl;
  std::cout << "Length: " << combined.length() << std::endl;

  // String comparison
  bool equal = (str1 == str2);
  std::cout << "Are the strings equal? " << equal << std::endl;

  // Conversion functions
  int num = std::stoi("123");
  double dbl = std::stod("3.14");
  std::cout << "Converted integer: " << num << std::endl;
  std::cout << "Converted double: " << dbl << std::endl;

  // Character manipulation
  char c = 'a';
  char upper = std::toupper(c);
  std::cout << "Uppercase of 'a': " << upper << std::endl;


  return 0;
}


