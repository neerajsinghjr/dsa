/**
	Problem: Given an distinct integer's array where number can be repeated and you need to 		return the largest length of the mountain. 

	i.e, Mountain defines continuous flow of number in array wheareas the previous number is lesser than the current one and the current number is lesser than the next one. 

	for eg,
	array = [5, 6, 1, 2, 3, 4, 3, 2, 0, 1, 2, 3, -2, 4]	
	here, 
	arr[0] = 5 
	arr[1] = 6
	arr[2] = 1

	So, Mountain Peak = arr[0] < arr[1] && arr[1] < arr[2];

**/

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int getMountainLength(vector<int>arr) {

	int largest = 0; 

	for(int x=0; x<arr.size()-2; x++) {
		
		if(arr[x] < arr[x+1] && arr[x+1] > arr[x+2]) {
			
			int count = 1;	// PEAK;

			// BACKWARD TRACKING;
			int y = x + 1;	// From PEAK Index;
			while(y > 0 && arr[y] > arr[y-1]) {
				count++;
				y--;
			}

			// FORWARD TRACKING;
			int z = x + 1;	// From PEAK Index;
			while(z < arr.size() && arr[z] > arr[z+1] ) {
				count++;
				z++;
			}

			// PEAK Largest Length;
			largest = max(largest, count);
		}

	} // End of For Loop;

	return largest;
}	//end of func;

int main() {
	int size, temp; 
	vector<int> arr;     //{5, 6, 1, 2, 3, 4, 3, 2, 0, 1, 2, 3, 2, 4};
	// Vector Size...;
	cout<<"\nVector's Size: ";
	cin>>size;
	// Vector In-Take...;
	for(int x=0; x<size; x++) {
		cout<<"\nVector["<<x<<"]: ";
		cin>>temp;
		arr.push_back(temp);
		cout<<endl;
	}
	cout<<"Mountain Peak: "<<getMountainLength(arr)<<endl;
	return 0;
}