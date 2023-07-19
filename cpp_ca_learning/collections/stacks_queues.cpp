#include <stdlib.h>

#include <iostream>

#include <queue>
// C++’s built-in std::stack lives in the <stack> standard library
#include <stack>



int main()
{
    // declaring a stack
    std::stack<int> plates;
    // adding elements to a stack
    plates.push(10);
    plates.push(8);
    plates.push(5);
    // removing elements from a stack
    plates.pop();
    // accessing elements
    std::cout << plates.top() << std::endl; // returns reference to top element
    // Unlike vectors, stack access is limited to the top element and cannot use index access.
    std::cout << plates.size() << std::endl; // size of stack
    std::cout << plates.empty() << std::endl; // 0 = non-empty, 1 = empty
    // swapping stacks
    


    // declaring a queue
    std::queue<std::string> line;
    // adding elements to a queue
    line.push("Amy");
    line.push("Bella");
    line.push("Chloe");  // "Chloe" -> "Bella" -> "Amy" (front element)
    // removing elements from a queue
    line.pop();  // "Chloe" -> "Bella" (front element)
    // accessing elements
    std::cout << line.front() << std::endl; // returns reference to front element
    std::cout << line.back() << std::endl; // returns reference to back element
    // Unlike vectors, queue access is limited to the front and back elements.

    std::cout << line.size() << std::endl; // size of queue
    std::cout << line.empty() << std::endl; // 0 = non-empty, 1 = empty

    return 0;
}
