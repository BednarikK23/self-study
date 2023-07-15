#ifndef CPP_CA_LEARNING_SONG_H
#include <iostream>
#include <string>


// add the Song class here:
class Song {
  std::string title;
  public:
    void add_title (std::string);
    std::string get_title();
};

/*
 * Constructors
 * Is there a way to give an object some data right when it gets created? We’re so glad you asked!
 * A constructor is a special kind of method that lets you decide how the objects of a class get created.
 * It has the same name as the class and no return type.
 * Constructors really shine when you want to instantiate an object with specific attributes.
 */

class City {
  std::string name;
  int population;

  public:
    // default constructor ensures proper initialization
    City() {
      name = "Default name";
      population = 0;
    }
    City(std::string new_name, int new_pop);
    std::string get_name() { return name; }
    int get_population() { return population; }

    // Destructor
    /*
     * another special method that is automatically called when an object is destroyed.
     * When an object moves out of scope or is explicitly deleted, the destructor will help with any clean-up work and
     *  prevent memory leaks before the object is removed from memory.
     *
     * Like a constructor, it has the same name as the class and no return type, but is preceded by a ~ operator and takes no parameters:
     */
    ~City() { // ~ -> altgr + +(1)
      std::cout << "Goodbye, " << name << "!\n";
    }
    // if this defined in another file then type is ~City::~City() { ... }
    // in the morning continue here:
    // https://www.codecademy.com/courses/c-plus-plus-for-programmers/articles/inheritance-cpp
};

/*
 * // city.cpp
  City::City(std::string new_name, int new_pop)
    // members get initialized to values passed in
    : name(new_name), population(new_pop) {}
  You could also write the definition like this:
  City::City(std::string new_name, int new_pop) {
    name = new_name;
    population = new_pop;
  }


 */



#define CPP_CA_LEARNING_SONG_H

#endif //CPP_CA_LEARNING_SONG_H
