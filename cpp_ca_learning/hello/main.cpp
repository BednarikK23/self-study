/*
 *  1) C system headers
 *  2) C++ standard library headers
 *  3) User-defined libraries’ headers.
 *
 * */


// user-defined classes and functions -> PascalCase
// variables -> snake_case

// brackets same rules as in C

// spacing  -> two spaces indentation
//          -> one line to separate functions

// this will be hello world from second tutorial

#include <iostream> // # for the preprocessor
using namespace std; // The above line introduces the namespace std into the current program.
                // This line allows the usage of standard library objects without prepending the std:: identifier.

int main() {
    cout << "Hello, world!";
    return 0;
}

// Incorrect syntax - we cannot declare int and double in the same statement
// int a = 1, double b = 2.3;

// Correct syntax
// int a = 1;
// double b = 2.2;

// It’s impossible to inadvertently change the value of a constant variable after it has been declared:
// const double pi = 3.14;

/*
Op	Name	        Example	Description
+	Addition	    x + y	x plus y
-	Subtraction	    x - y	x minus y
*	Multiplication	x * y	x multiplied by y
/	Division	    x / y	x divided by y
%	Modulus	        x % y	The remainder of x divided by y
++	Pre-increment	++x	    Increment x, then return x
--	Pre-decrement	--x	    Decrement x, then return x
++	Post-increment	x++	    Copy x, then increment x, then return the copy
--	Post-decrement	x--	    Copy x, then decrement x, then return the copy
 */

// Difference between pre and post ops is the same as in C:
/*
 * int x = 5;
 * int y = ++x; // x will change to 6 and then assign to y
 * int z = x++; // x will assign to z and then change to 7
 */

/*
 * *=
 * /=
 * +=
 * -=
 * same as in Python
 *
 */


// Bitwise and logical operators same as in C

