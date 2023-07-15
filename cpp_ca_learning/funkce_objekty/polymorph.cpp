#include <iostream>

// POLYMORPHISM
/*
 * The term polymorphism means “many forms”. In C++, polymorphism applies to class methods in an inheritance relationship.
 *
 * Polymorphism allows a derived class to override methods inherited from its base class.
 * Although they have the same function signature, the C++ compiler will resolve function execution depending on the type of object that invokes the function.
 */

class Animal {
public:
    void action() {
      std::cout << "The animal does something.\n";
    }
};

class Fish: public Animal {
public:
    void action() {
      std::cout << "Fish swim.\n";
    }
};

class Bird: public Animal {
public:
    void action() {
      std::cout << "Birds fly.\n";
    }
};

int main() {
  Animal newAnimal;
  Fish newFish;
  Bird newBird;

  newAnimal.action();
  newFish.action();
  newBird.action();

  return 0;
}

/*
 * The two derived classes Fish and Bird both inherit the action() method from the base class Animal.
 * However, each class has its own unique implementation of this method.

 * In other words, the action() method has “polymorphed” into three different forms.
 * The type of the caller object determines which form of action() is executed.
 */
