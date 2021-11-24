/**
	Problem: Return a triplets for a target sum in ascending order.
	like,
	array = [1,2, 3, 4, 5, 6, 7, 9, -3, 1, -2]
	target = 6
	output: Should be sorted Vertically & Horizontally...
	[-2, 1, 7]
	[1, 2, 3]
*/

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

/*** Generate Triplets ***/
vector<vector<int>> getTriplets(vector<int> arr, int target)
{
	vector<vector<int>> result;
	// Sort - O(nlogn)
	sort(arr.begin(), arr.end());
	// Outer Loop - O(n)
	for (int x = 0; x < arr.size() - 2; x++)
	{
		int startIndex = x + 1;
		int endIndex = arr.size() - 1;
		int lookupSum = target - arr[x];
		// Inner Loop - O(n)
		while (startIndex < endIndex)
		{
			int currentSum = arr[startIndex] + arr[endIndex];
			if (currentSum == lookupSum)
			{
				result.push_back({arr[x], arr[startIndex], arr[endIndex]});
				startIndex += 1;
			}
			else if (currentSum < lookupSum)
			{
				startIndex += 1;
			}
			else if (currentSum > lookupSum)
			{
				endIndex -= 1;
			}
		} // Inner Loop;
	}	  // Outer Loop;
	return result;
}

/*** Main Execution ***/
int main()
{
	int target, size, temp;
	vector<int> arr;
	// Input Target;
	cout << "\nTarget: ";
	cin >> target;
	// Input Size;
	cout << "\nSize: ";
	cin >> size;
	// Input Vector;
	for (int x = 0; x < size; x++)
	{
		cout << "\nVector[" << x + 1 << "]: ";
		cin >> temp;
		arr.push_back(temp);
	}
	// Printing Array;
	auto triplets = getTriplets(arr, target);
	cout << "\nResult:" << endl;
	for (auto triplet : triplets)
	{
		for (auto item : triplet)
		{
			cout << item << "\t";
		}
		cout << endl;
	}
	return 0;
}