/*
* File: Review.h
*
* Description: A review of C ++; header and implementation file, methods,
* arrays, loops, calculations, pointers, strings, constructor, destructor.
*
* Completion time: 2 hours
*
* @author: Ivan Fernandez
* @version: 1.0
* Assignment: Review C ++
*
* Date: 10/6/2019
*/

#ifndef REVIEW_H
#define REVIEW_H

#include <cstring>
#include <string>

class Review
{
    public:
        Review(double a, double b, std::string s);
        virtual ~Review();
        void addition();
        void subtraction();
        void reverseString();
    protected:
    private:
        double a;
        double b;
        double sum;
        double sub;
        std::string s;
};

#endif // REVIEW_H
