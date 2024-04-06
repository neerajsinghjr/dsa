````
-------------------------------------------------------------------------------------
-> Title : NEETCODE MASTER DSA NOTES    
-> Author : @neeraj-singh-jr
-> Status : Ongoing...
-> Created : 2024-03-17
-> Updated : 2024-04-07
-> Summary : Notes indices are as follows (**** pending)
-------------------------------------------------------------------------------------
-> Q004 : Usage of 2^n combination for substring or subsequence problem;;
-> Q003 : Anagram in DSA Problems;;
-> Q002 : Pallindrome in DSA Problems;;
-> Q001 : Subarray and Subsequence in DSA Problems;;
-------------------------------------------------------------------------------------
````

### NEETCODE MASTER DSA NOTES : BEGINNING

-------------------------------------------------------------------------------------
### Q004 : Usage of 2^n combination for substring or subsequence problem;;

In the context of algorithms or problems involving substrings or subsequences, the 
expression `2^(right-left)`, often arises when counting the number of possible 
substrings or subsequences within a given range defined by the variables left and right.

> Here's an explanation:

1. `Substrings or Subsequences`: A substring is a contiguous sequence of characters 
within a string. A subsequence is a sequence that can be derived from another sequence 
by deleting some or no elements without changing the order of the remaining elements


2. `Counting Possible Subsequences`: When you have a string or an array. You're trying 
to count the number of possible substrings or subsequences within a given range, you 
often iterate through the range with two pointers, `left` and `right`. Each substring 
or subsequence corresponds to a contiguous segment between these two pointers.


3. `Calculating the Count`: The expression `2^(right-left)`, represents the number of 
possible substrings or subsequences that can be formed using the characters or elements 
between the left and right pointers. This is because for each character or element in 
the range, you have two choices: include it in the subsequence or exclude it. 
Therefore, the total number of combinations is `2^(right-left)`


4. `Example` : Let's say you have a string "abc". If left = 0 and right = 2, then you 
have substrings "a", "ab", "abc", "b", "bc", and "c". 
The count of substrings is `2^(2-0)=4`, which includes all combinations of including 
or excluding characters between the left and right pointers.


> Conclusion:
 
This approach is commonly used in algorithms like sliding window, two pointers, or 
dynamic programming to efficiently calculate counts of substrings or subsequences. 

It's important because it allows you to avoid explicitly generating and checking every 
possible substring or subsequence, which would be inefficient for large inputs. 

Instead, you can calculate the count directly based on the range of indices



-------------------------------------------------------------------------------------
### Q003 : Anagram in DSA Problems;;

- An anagram is a word or phrase formed by rearranging the letters of another word 
or phrase, using all the original letters exactly once. In other words, an anagram 
is a permutation of the letters of a word or phrase.
- Anagrams retain the same set of characters as the original word or phrase, but 
in a different order.
- for eg,
````
# anagrams examples ... 
"listen" and "silent", 
"debit card" and "bad credit" 
"cinema" and "iceman" 

# NOTE: above mentioned anagram have same set or character only just 
# rearranging for letters taken place in formation for new words;;
````

-------------------------------------------------------------------------------------
### Q002 : Pallindrome in DSA Problems;;

- A palindrome is a word, phrase, number, or other sequence of characters that reads 
the same forward and backward. In other words, a palindrome remains unchanged when 
read backward.

- For eg,
````
# palindromic words ...
"radar", "level", "noon", "deified"

# palindromic phrases ...
"A man, a plan, a canal, Panama!", 
"Madam, in Eden, I'm Adam", 
"Was it a car or a cat I saw?".

# pallindromic numbers, where the digits read the same forward and backward ... 
`121, 1331, 12321`, 

````

-------------------------------------------------------------------------------------
### Q001 : Subarray and Subsequence in DSA Problems;;

#### Subarray:-
- A subarray is a contiguous part of an array.
- Subarrays are always contiguous, meaning they consist of consecutive elements 
from the original array.

For example, consider the array 
````
nums = [1, 2, 3, 4] 
Its subarrays include ...
[1], [2], [3], [4], 
[1, 2], [2, 3], [3, 4], 
[1, 2, 3], [2, 3, 4], 
[1, 2, 3, 4], and more.
````

#### Subsequence:-

- A subsequence is a sequence that can be derived from another sequence by deleting 
some or no elements without changing the order of the remaining elements.
- Subsequences can have different lengths and may or may not be contiguous.
for eg,
````
nums = [1, 2, 3]
Its subsequences include... 
[], 
[1], [2], [3], 
[1, 2], [1, 3], [2, 3], 
[1, 2, 3],  
Note: Empty Sequence is also an subarray for the given sequence.
````

#### Difference in Subsequence vs Subarray:-

- The main difference between subsequences and subarrays lies in their contiguity. 
Subsequences can skip elements and are not necessarily contiguous, while subarrays are 
always contiguous and consist of consecutive elements from the original array.
- A subsequence can be derived by deleting some or no elements from the original sequence 
without changing the order of the remaining elements.
- A subarray is a contiguous part of an array, meaning it consists of consecutive elements 
from the original array.
- Subsequences may not be contiguous, while subarrays are always contiguous.

-------------------------------------------------------------------------------------