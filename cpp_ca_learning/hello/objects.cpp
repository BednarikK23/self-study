#include <stdlib.h>
#include <string>
#include <iostream>

#include "song.h"

/*
 * For larger projects, it’s recommended to split up the class definition in a header and a .cpp file.
 * Doing so requires class methods to be defined outside of the class definition.
 * In this scenario, use the ClassName:: namespace to indicate that the function belongs to that class.

 * For example, if the banner() function was defined separately, it would look like this:

void School::banner() {
  std::cout << name << " is " << age << " years old.\n";
}

 Note: Even though a method can be defined outside its class, it must still be declared inside it.

 */

void Song::add_title(std::string new_title) {
  title = new_title;
}

std::string Song::get_title() {
  return title;
}
// https://www.codecademy.com/courses/learn-c-plus-plus/lessons/cpp-classes-and-objects/exercises/cpp-class-members

// Constructor continue -> described in song.h
City::City(std::string new_name, int new_pop)
  : name(new_name), population(new_pop) {}

// members get initialized to values passed in
// also could be written like this:
// City::City(std::string new_name, int new_pop) {
//   name = new_name;
//   population = new_pop;
// }



/*
 * ACCESS SPECIFIERS
 * By default, everything in a class is private, meaning class members are limited to the scope of the class.
 * But sometimes you need access to class members, and for that, there is public.
 */


//To create a class, use the class keyword in the following syntax:
class School {
  //The public keyword is an access specifier that allows members of School to be directly accessed outside the class.
  public:
    std::string name;
    int age;

    void banner() {
      std::cout << name << " is " << age << " years old.\n";
    }
}; // <- don't forget the semicolon

// The components of a class are called class members. There are two types of class members:
//
// 1) Attributes, also known as member variables, contain information about an object of the class.
// 2) Methods, also known as member functions, are functions that belong to the class.


int main() {
  //Creating an object is very similar to creating a variable; simply specify the class name followed by the object name.
  School codeacademy;
  codeacademy.name = "Codecademy";
  codeacademy.age = 8;

  codeacademy.banner();

  return 0;
}





