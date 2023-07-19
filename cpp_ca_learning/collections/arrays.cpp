#include <stdlib.h>

#include <iostream>

// In C++, an array is a fixed-sized collection of items of the same type




int main()
{
    // declarace pole je stejna jak v c
    int arr[5];

    // pokud rovnou i inicilizujeme, tak počet prvku muž byt vynechan a pole bude mit fixni velikost o tolika prvcích..:
    int arr2[] = {1, 2, 3, 4, 5};

    // accessing elements je jasny
    std::cout << arr2[0] << std::endl;

    // multidimensional:
    int table[3][5] = {
            {0, 1, 2, 3, 4} ,
            {5, 6, 7, 8, 9} ,
            {10, 11, 12, 13, 14}
    };

    // iterating over array:
    int fibonacci[5] = {0, 1, 1, 2, 3};
    for (int i = 0; i < 5; i++) {
        std::cout << fibonacci[i];
    }
    // for each loop kinda cool:
    for (int num: fibonacci) {
        std::cout << num;
    }

    // 2D
    char game[3][3] = {
            {'x', 'o', 'o'} ,
            {'o', 'x', 'x'} ,
            {'o', 'o', 'x'}
    };

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            std::cout << game[i][j];
        }
        std::cout << "\n";
    }




    return 0;
}


