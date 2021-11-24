/**
	Problem: Merge two sorted array into one array...
	like,

	merge = [1,2,3,4] and [5,6] => [1,2,3,4,5,6]

**/
#include <iostream>

using namespace std;

/** Get Array **/
int *getArray(int arr[], int size) {
    cout<<"Array Insertion..."<<endl;
    for (int x=0; x<size; x++) {
        cin>>arr[x];
    }
    return arr;
}

/** Main Execution **/
int main() {
    cout<<"main";
    int L1, L2;
    cout<<"First Array Size: ";
    cin>>L1;
    cout<<"Second Array Size:";
    cin>>L2;
    int first[L1], second[L2];
    first[L1] = getArray(first, L1);
    second[L2] = getArray(second, L2);
    return 0
}
