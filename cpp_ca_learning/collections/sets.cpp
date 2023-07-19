#include <stdlib.h>

#include <iostream>
#include <set>
#include <unordered_set>

// set is a data structure that stores multiple unique elements in a single variable.
// Elements of a set are not accessible by index like vectors. Instead, they are accessible by key values.
// In a set, the value of each element acts as its own key that uniquely identifies it.


/*
 * Two types of sets in c++:
 * 1) std::set: Implements a sorted set using a balanced binary search tree (usually a Red-Black Tree).
 *    The elements in a std::set are ordered according to a strict weak ordering criterion defined by the comparison function or operator provided.
 * 2) std::unordered_set: Implements an unordered set using a hash table.
 *    The elements in an std::unordered_set are not ordered, but they are stored based on their hash values.
 *
 * Usage:
 * 1) std::set: Suitable when maintaining elements in a sorted order is important
 *              or when you need to perform range-based operations (e.g., finding elements within a specific range).
 * 2) std::unordered_set: Useful when the order of elements is not important, but fast insertion, deletion, and lookup times are required.
 *
 * There are same functions for both sets:
 * 1) insert(): Inserts an element into the set.
 * 2) erase(): Removes an element from the set.
 * 3) find(): Searches the set for a given element and returns an iterator to it if found.
 * 4) size(): Returns the number of elements in the set.
 * 5) empty(): Returns true if the set is empty.
 * 6) clear(): Removes all elements from the set.
 * 7) count(): Returns 1 or 0 based on whether an element is present in the set or not.
 * 8) begin(): Returns an iterator to the first element in the set.
 * 9) end(): Returns an iterator to the element following the last element in the set.
 */


int main()
{
    // declaring a set
    std::unordered_set<int> prims;
    // declaration & initialization
    std::unordered_set<int> primes({2, 3, 5, 5, 7}); // contains 2, 3, 5, 7 - cause cannot contain duplicates

    // adding elements
    primes.insert(2);
    primes.insert(3);
    primes.insert(3);  // Duplicate value is not inserted

    // removing elements
    primes.erase(3);  // removes 3 from the set

    // searching for an element
    // The .count() function searches in the set and returns the number of elements that match the argument value.
    if (primes.count(4))
        std::cout << "4 is a prime";
    else
        std::cout << "4 is not a prime";

    std::cout << primes.size() << std::endl; // size() - returns the number of elements in the set
    std::cout << primes.empty() << std::endl; // empty() - returns 1 if the set is empty else 0

    // iterating over set
    std::unordered_set<int> numbers({1, 3, 5, 7, 9});
    for (int number: numbers) {
        std::cout << number << " ";
    }

    return 0;
}


