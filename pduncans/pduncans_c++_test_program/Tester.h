/*
    Tester.h is designed to demonstrate a class creation
    system in c++.

    @author Paul Duncanson
    @version 1.0
*/

#ifndef TESTER_H
#define TESTER_H

#include <string>

using namespace std;

class Tester{
    private:
        int number;
        string word;
    public:
        Tester(int num, string chars);
        int getNumber();
        string getWord();
};



#endif
