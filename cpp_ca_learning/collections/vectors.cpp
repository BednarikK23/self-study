#include <stdlib.h>

#include <iostream>
#include <vector>

/*
 * Similar to an array, a vector is used to store a sequence of elements accessible by index.
 * But unlike arrays, vectors can dynamically shrink and grow in size.
 * Elements can be added or removed from a vector after it has been declared.
 */

int main()
{
    // declaring a vector
    std::vector<int> weights;
    // The type of the vector cannot be changed after the declaration.

    // initializing a vector
    std::vector<char> alphabet = {'a', 'b', 'c'};

    // adding elements to a vector
    alphabet.push_back('d');
    weights.push_back(10);

    // removing elemetn from a vector
    alphabet.pop_back();

    // accessing elements
    std::cout << alphabet[1] << weights[0] << std::endl;

    std::cout << alphabet.back() << std::endl;   // returns reference to last element
    std::cout << alphabet.size() << std::endl;   // size of vector
    std::cout << alphabet.empty() << std::endl;  // 0 = non-empty, 1 = empty
    std::cout << alphabet.front() << std::endl;  // first element


    // iterating over vector
    std::vector<char> vowels = {'a', 'e', 'i', 'o', 'u'};
    for (int i = 0; i < vowels.size(); i++) {
        std::cout << vowels[i] << " ";
    }
    // for each loop:
    for (char letter: vowels) {
        std::cout << letter << " ";
    }

    return 0;
}
