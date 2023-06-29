#include <iostream>
#include <stdlib.h>
#include <ctime>

int main() {
    /*
     * Data types:
     * int
     * double
     * char
     * string
     * bool
     **/


    // To compile: g++ hello.cpp -o hello
    // std::cout is the “character output stream”. It is pronounced “see-out”.
    char space = ' ';
    std::cout << "Hello" << space << "World!\n" << std::endl;
    // this is called chaining... you can chain as many as you want threw <<
    // also you can write string litterals onto many lines, each line have to be in double quotes...
    // on the end then has to be std::endl;

    int tip = 0;

    std::cout << "Enter amount: ";
    std::cin >> tip;
    // std input stream - for character input


    /**
    An if statement checks a condition and will execute a task if that condition evaluates to true.
    if / else statements make binary decisions and execute different code blocks based on a provided condition.
    We can add more conditions using else if statements.
    Relational operators, including <, >, <=, >=, ==, and != can compare two values.
    A switch statement can be used to simplify the process of writing multiple else if statements.
    The break keyword stops the remaining cases from being checked and executed in a switch statement.
    */

    srand (time(NULL));
    int	coin = rand() % 2;
    if (coin == 0) {
        std::cout << "Heads\n";
    } else if (coin == 3) {
        std::cout << "Edge\n";
    } else
        std::cout << "Tails\n";

    int grade = rand() % 10;
    switch (grade) {
        case 9:
            std::cout << "Freshman\n";
            break;
        case 10:
            std::cout << "Sophomore\n";
            break;
        case 11:
            std::cout << "Junior\n";
            break;
        case 12:
            std::cout << "Senior\n";
            break;
        default:
            std::cout << "Invalid\n";
            break;
    }

    // LOOPS:
    // while, for uplne stejne jak v cčku,
    // do while je taky stejny jak vsude jinde...
    // break, continue...


    // ERRORS:
    // Compile-time errors: Errors found by the compiler.
    // Run-time errors: Errors found by checks in a running program.
    // Logic errors: Errors found by the programmer looking for the causes of erroneous results.
    // Link-time errors: Errors found by the linker when it is trying to combine object files into an executable program.

    // vectors and arrays.., i will switch to harder course now...


    return 0;
}
