#include <stdlib.h>

#include <iostream>
#include <map>
#include <unordered_map>

// hash map is a data structure that stores a collection of elements formed by a combination of a key value and a mapped value.
// Each key value acts as a unique identifier for the element, while the mapped value is the content associated with this key.


/*
 * 1) Underlying Data Structure:
 *  a) std::map: Implements a sorted associative container using a balanced binary search tree (usually a Red-Black Tree).
 *      The elements in a std::map are ordered based on the keys according to a strict weak ordering criterion defined by the comparison function or operator provided.
 *  b) std::unordered_map: Implements an unordered associative container using a hash table.
 *      The elements in an std::unordered_map are not ordered, but they are stored based on the hash values of the keys.
 *
 * 2) Usage:
 *  a) std::map: Suitable when maintaining elements in a sorted order based on keys is important or
 *      when you need to perform range-based operations (e.g., finding elements within a specific key range).
 *  b) std::unordered_map: Useful when the order of elements is not important, but fast insertion, deletion, and lookup times based on keys are required.
 */


int main()
{
    // Declare an unordered map with string keys and integer values
    std::unordered_map<std::string, int> codes;
    // with initialization
    std::unordered_map<std::string, int> country_codes(
            {{"India", 91},
             {"Italy", 39}});

    // adding elements
    //  a) insert() method
    // since hash maps cannot contain duplicate keys, an element is inserted only if its key is not equivalent
    // to any of the other elements already in the container.
    country_codes.insert({"Thailand", 66});
    country_codes.insert({"Peru", 51});
    country_codes.insert({"Peru", 9});    // Duplicate key is not inserted
    // b) [] operator
    // Normally, [] is used to access existing elements in the hash map.
    // However, if the key specified inside [] does not match the key of any element in the container, the function inserts a new element with that key
    country_codes["Thailand"] = 66;
    country_codes["China"] = 86;

    // removing elements
    // a) erase() method
    country_codes.erase("Thailand");
    // b) clear() method
    country_codes.clear(); // removes all elements from the hash map

    // just adding something back...
    country_codes["Argentina"] = 54;
    country_codes["Belgium"] = 32;

    // checking if an element is present
    // The .count() function searches in the hash map and returns the number of elements whose key matches the argument value.
    if (country_codes.count("Belgium"))
        std::cout << "There is a code for Belgium";
    else
        std::cout << "There isn't a code for Belgium";

    // size
    std::cout << country_codes.size() << std::endl;
    std::cout << country_codes.empty() << std::endl;

    // iterating over hash map
    // The elements in a hash map are not ordered, so you cannot use the [] operator to access elements.
    // Instead, you can use the .at() function to access elements by key.
    for(auto it = country_codes.begin(); it != country_codes.end(); ++it) {
        std::cout << it->first << " " << it->second << std::endl;
    }
    // for each loop:
    for (auto it: country_codes) {
        std::cout << it.first << " " << it.second << std::endl;
    }
    // for each loop (C++17):
    for (const auto& [key, value]: country_codes) {
        std::cout << key << " " << value << std::endl;
    }

    return 0;
}
