/**
	Problem: Given an distict array of variable size which can have a duplicate number as possible.
    You need to find the longest chain in the array with different of next and previous element is 1.

    Like, 
    for e.g,
    array = 14, 15, 1, 3, 5, 6, 18, 19, 2, 7, 20, 8, 21, 9, 10 , 4

    Longest Continue chain in unit difference like...
    Total, 10 = [1 => 2 => 3 => 4 => 5 => 6 => 7 => 8 => 9 > 10]
    
    Other Chain like, [14 => 15] and [18 => 19 => 20 => 21]

**/

#include <iostream>
#include <algorithm>
#include <unordered_set>
#include <vector>

using namespace std;

int getLongestBand(vector<int> arr) {
	int len=arr.size(), largest = 1;
	unordered_set<int> uset;

	// Insert Unordered_Set - O(n)
	for(auto a: arr) {
		uset.insert(a);
	}

	// Find Elements - O(n)
	for(int x=0; x<len; x++) {
		// Checkpoint For Parent Element;
		// if (!(uset.find(arr[x]-1) != uset.end())) {
		if (uset.find(arr[x]-1) == uset.end()) {
			int count = 1;
			int lookup = arr[x] + 1;

			while(uset.find(lookup) != uset.end()) {
				lookup++;
				count++;
			}	// End of While Loop

			largest = count > largest ? count : largest;
        }
	}	//End of For Loop;
	
	return largest;
}

int main() {
	int size, temp;
	vector<int> arr;    //{14, 15, 1, 3, 5, 6, 18, 19, 2, 7, 20, 8, 21, 9, 10 , 4, 22, 23, 24};
	cout<<"Vector's Size: ";
	cin>>size;
	for(int x=0; x<size; x++) {
		cout<<"Vector["<<x<<"]: ";
		cin>>temp;
		arr.push_back(temp);
	}
	int result = getLongestBand(arr);
	cout<<"Longest Band: "<<result<<endl;
	return 0;
}