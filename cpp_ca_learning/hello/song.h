#ifndef CPP_CA_LEARNING_SONG_H
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
    City(std::string new_name, int new_pop);
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
