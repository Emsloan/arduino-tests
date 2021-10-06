/*
* File: main.cpp
*
* Description: A program testing and reviewing various
* functions in C ++.
*
*
* Completion time: 2 hours
*
* @author: Ivan Fernandez
* @version: 1.0
* Assignment: Review C ++
*
* Date: 10/6/2021
*/



#include "Review.h"
#include "Review.cpp"


#include <cstring>
#include <iostream>
#include <string>

using namespace std;

int main()
{
    double a;
    double b;
    string s;

    cout << "Please enter the first number.\n";
    cin >> a;

    cout << "Please enter the second number.\n";
    cin >> b;

    cout << "Please enter a string. \n";
    cin >> s;


    Review rev(a, b, s);

    rev.addition();
    rev.subtraction();
    rev.reverseString();

    return 0;
}
