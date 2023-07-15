/*
 * inheritance is the concept of defining a class in terms of another class.
 * Inheritance makes it possible to reuse code and to establish hierarchical relationships between classes.
 */

#include <iostream>

/*
 * Basic Inheritance
Classes that belong to an inheritance relationship are separated into two groups:

1) Base class or parent class: The class being inherited from.
2) Derived class or child class: The class that inherits from the base class.
A derived class inherits attributes and methods from its base class.
 To declare a derived class, place : after the class name ->
        -> then write the access specifier and the name of the base class:
 */

// Base class
class Animal {
private:
    std::string gender;
    int age;

public:
    Animal(std::string new_gender, int new_age)
        : gender(new_gender), age(new_age) {}
};

// Derived class
class Dog: public Animal  {
private:
    std::string breed;

public:
    // Call base class constructor
    Dog(std::string new_gender, int new_age, std::string new_breed)
        : Animal(new_gender, new_age), breed(new_breed) {}

    void sound() {
      std::cout << "Woof\n";
    }
};
// * Dog class inherits the attributes gender and age from the Animal class.
// * The Dog class also has a new breed attribute and a new sound() function of its own.
int main2(); // just forward declaration skip this line...

int main() {
  Dog buddy("male", 5, "Bulldog");

  buddy.sound(); // Outputs: Woof
  main2();
  return 0;
}

// MULTILEVEL INHERITANCE
// A class can inherit from another class that is already derived from another class.
// This concept is sometimes referred to as an inheritance chain:
class A {    // A is the base class
public:
  int a;

  A() { std::cout << "Constructing A\n"; }
};

class B: public A {    // class B inherits from class A
public:
  int b;

  B() { std::cout << "Constructing B\n"; }
};

class C: public B {    // class C inherits from class B
public:
  int c;

  C() { std::cout << "Constructing C\n"; }
};

//In an inheritance chain, the “most base” class is always constructed first.
// The order of class construction then goes from the parent to the child.
int main2() {
  C example;
  // -> Constructing A
  //    Constructing B
  //    Constructing C

  return 0;
}

// SPECIFIERS / Types of Inheritance
/*
 * When declaring a derived class, the base class may be inherited through three different types of inheritance:

  Public Inheritance: The access specifiers of the base class members stay the same in the derived class. This is the most commonly used type of inheritance.
  Protected Inheritance: public and protected members of the base class become protected members of the derived class.
  Private Inheritance: All base class members become private members of the derived class.
  The following table is a reminder of the three access specifiers in C++:

  Access	              public	protected	  private
  Inside the class	      yes	      yes	      yes
  Inside derived classes	yes	      yes	      no
  Outside the class	      yes	      no	      no
 */
