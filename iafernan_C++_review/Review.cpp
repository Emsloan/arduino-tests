/*
* File: Review.cpp
*
* Description: A review of C ++; header and implementation file, methods,
* arrays, calculations, loops, strings, pointers, constructor, destructor.
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


#include <iostream>
#include <cstring>
#include <string>

using namespace std;

Review::Review(double a, double b, string s)
{
    //ctor
    this->a = a;
    this->b = b;
    this->s = s;
}

Review::~Review()
{
    //dtor
    cout << "Class deconstruction." << endl;
}

void Review::addition()
{
    this->sum = this->a + this->b;
    cout << "The sum of the numbers is " << sum << endl;

}

void Review::subtraction()
{

    this->sub = this->a - this->b;
    cout << "The difference of the numbers is " << sub << endl;


}

void Review::reverseString()
{
    int c = this->s.length();

    for (int i=0; i < c/2; i ++)
        swap(this->s[i], this->s[c-i-1]);

    cout << "The reverse of the string: " << this->s << endl;


}
