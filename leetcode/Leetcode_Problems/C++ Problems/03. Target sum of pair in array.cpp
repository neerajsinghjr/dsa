/**
	Problem: Given an array, in which any two pair gives the equivalent target sum,
	Like,
	array = [12, 13, 14, 15, 16]
	target = 26
	output = [12,14]
**/

#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

// Generate Pair;
vector<int> getPairs(vector <int> arr, int sum) {

	int look;
	vector<int> result;
	unordered_set<int> uSet;
	for(int num: arr) {
		look = sum - num;
		if(uSet.find(look) != uSet.end()) {
				result.push_back(num);
				result.push_back(look);
				return result;
		}
		uSet.insert(num);
	}

	return result;
}

// Main Execution;
int main() {
	int size, value, sum;
	vector<int> arr;
	cout<<"Target Sum: ";
	cin>>sum;
	cout<<"Vector Size: ";
	cin>>size;
	for(int i=0; i<size; i++) {
		cout<<"Vector["<<i+1<<"]: ";
		cin>>value;
		arr.push_back(value);
		cout<<endl;
	}
	auto output = getPairs(arr, sum);
	if(output.empty()) {
		cout<<"NOT FOUND!!";
	}else{
		cout<<"Pairs: "<<output[0]<<","<<output[1]<<endl;
	}
}
