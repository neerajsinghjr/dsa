````
-------------------------------------------------------------------------------------
-> Title : NEETCODE MASTER DSA NOTES    
-> Author : @neeraj-singh-jr
-> Status : Ongoing...
-> Created : 2024-03-17
-> Updated : 2024-03-17
-> Summary : Notes indices are as follows (**** pending)
-------------------------------------------------------------------------------------
-> Q003 : Anagram in DSA Problems;;
-> Q002 : Pallindrome in DSA Problems;;
-> Q001 : Subarray and Subsequence in DSA Problems;;
-------------------------------------------------------------------------------------
````

### NEETCODE MASTER DSA NOTES : BEGINNING

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