/*
    Tester.cpp is designed to demonstrate a class creation
    system in c++.

    @author Paul Duncanson
    @version 1.0
*/

#include "Tester.h"

using namespace std;

Tester::Tester(int num, string chars){
    number = num;
    word = chars;
}

int Tester::getNumber(){
    return number;
}

string Tester::getWord(){
    return word;
}



