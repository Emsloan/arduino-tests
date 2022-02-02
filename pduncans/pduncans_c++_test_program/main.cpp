/*
    This program is designed to practice the C++ programming
    language.  This is the language used for creating arduino
    sketches.

    @author Paul Duncanson
    @version 1.0

*/

#include "Tester.h"
#include <iostream>

using namespace std;

int main(){

    //Create an array
    int nums[5];

    //Populate the Array
    for (int i = 0; i < sizeof(nums)/sizeof(nums[0]); i++){
        nums[i] = i * 2;
    }

    //Use pointers to traverse the array
    int* ptrNums = nums;

    cout << "---Array And Pointer Tests---" << "\n";
    for (int i = 0; i < sizeof(nums)/sizeof(nums[0]); i++){
        //Print value in array
        cout << "The value in index " << i << ": " << *ptrNums << "\n";
        // Print address of value
        cout << "The address is " << ptrNums << "\n\n";
        //Move to the next address
        ptrNums++;
    }

    //Create a tester class
    Tester tester(4, "Hello");
    cout << "\n---Class Tested---" << "\nTester number: " << tester.getNumber();
    cout << "\nTester word: " << tester.getWord() << "\n";

    return 0;
}
