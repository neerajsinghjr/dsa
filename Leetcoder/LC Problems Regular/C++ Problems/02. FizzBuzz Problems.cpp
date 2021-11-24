/**
    Problem: Create a Vector function which take a
    integer as input, and create a function based on
    centain condition...
    1. Multiple of 3, should print "Fizz"
    2. Multiple of 5, should print "Buzz"
    3. Mutliple of 3 and 5, should print "FizzBuzz"

    like,
    FizzBuzz = {
        1, 2, "Fizz", 4, "Buzz", ... , 14, "FizzBuzz"
    }
**/

#include <iostream>
#include <vector>
#include <typeinfo>
#include <string>

using namespace std;

// FizBuzz Generator;
vector<string> fizzbuzz(int n) {
    vector<string> arr;
    for (int x=0 ; x < n; x++) {
        // Multiple of 3 and 5;
        if((x+1) % 3 == 0 && (x+1) % 5 == 0) {
            arr.push_back("FizzBuzz");
        }
        // Multiple of 3;
        else if((x+1) % 3 == 0) {
            arr.push_back("Fizz");
        }
        else if((x+1) % 5 == 0) {
            arr.push_back("Buzz");
        }
        else {
            arr.push_back(to_string(x+1));
        }
    }
    return arr;
}

// Main Execution;
int main() {
    int num;
    cout<<"Enter Limit (Number): ";
    cin>>num;
    if (!isdigit(num)) {
        vector<string> result = fizzbuzz(num);
        for(string itr : result) {
            cout<<itr<<" \t";
        }
        cout<<endl;
    }else {
        cout<<"Error, We are expecting a number";
    }	
    return 0;
}