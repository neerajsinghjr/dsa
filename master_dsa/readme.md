````
-------------------------------------------------------------------------------------
-> Title : MASTER DSA NOTES    
-> Author : @neeraj-singh-jr
-> Status : Ongoing...
-> Created : 17/03/2024
-> Updated : 09/06/2025
-> Summary : Notes indices are as follows (**** pending)
-------------------------------------------------------------------------------------
-> Q015 : Understanding Bucket Sort Algorithm 
-> Q014 : Heap vs Monostack - Problem Identification
-> Q013 : Understanding Heap with DSA Problems Identification;;
-> Q012 : Anagram Array and Strings in DSA;;
-> Q011 : BitWise Right Shift Operator Dividing Usecase;;
-> Q010 : BitWise Left Shift Operator Multiplying Usecase;;
-> Q009 : Bitwise XOR Operator Swapping Usecase;;
-> Q008 : Boyer Moorie Algorithm In-Depth;;
-> Q007 : Monotonic Stacks Algorithms In-Depth;;
-> Q006 : Isomorphich arrays and strings in DSA;;
-> Q005 : Bitwise Manipulation in One Go;;
-> Q004 : Usage of 2^n combination for substring or subsequence problem;;
-> Q003 : Anagram in DSA Problems;;
-> Q002 : Pallindrome in DSA Problems  ;;
-> Q001 : Subarray and Subsequence in DSA Problems;;
-------------------------------------------------------------------------------------
````

### MASTER DSA NOTES : BEGINNING

-------------------------------------------------------------------------------------
### Q015 : Understanding Bucket Sort Algorithm 




-------------------------------------------------------------------------------------
### Q014 : Heap vs Monostack - Problem Identification

---

#### 1. Heap Problems (Priority Queue)

A **Heap** is a tree-based data structure that satisfies the heap property:
* **Min-Heap:** The value of each node is less than or equal to the values of 
its children (smallest element at the root).
* **Max-Heap:** The value of each node is greater than or equal to the values 
of its children (largest element at the root).

Heaps are typically used to implement **Priority Queues**.

**How to Identify a Heap Problem:**

Look for keywords and scenarios that indicate a need for efficiently 
retrieving the *smallest/largest element* (or K-smallest/K-largest) from a 
dynamic collection where elements are frequently added or removed.

* **"Top K" or "Kth Largest/Smallest" elements:** 
- This is the most classic indicator. If you need the `k` largest/smallest 
items from a potentially larger set, a min-heap (for largest) or max-heap 
(for smallest) is often the way to go.
- *Example:* 
    - Kth Largest Element in an Array
    - Top K Frequent Elements
    - K Closest Points to Origin.

* **Dynamic Minimum/Maximum:** 
- When you need to always access the current minimum or maximum value in 
a collection that is constantly changing (elements being added/removed).
- *Example:* 
    - Median of a Data Stream (uses two heaps: one min-heap, one max-heap).

* **Scheduling/Prioritization:** 
- Problems where tasks or elements have priorities, and you always need to 
process the one with the highest (or lowest) priority next.
- *Example:* 
    - Dijkstra's shortest path algorithm
    - Prim's minimum spanning tree algorithm
    - Job Scheduling.

* **Merging Sorted Structures:** 
- When you need to merge `K` sorted arrays or linked lists efficiently. A 
min-heap helps you always pick the smallest available element across all 
lists.
- *Example:*
    - Merge K Sorted Lists/Arrays.

* **Any time you see "priority queue":** This is a direct hint.

**Key Heap Characteristics:**

* **Global Extremum:** 
Provides quick access ($O(1)$) to the absolute min/max element.
* **Logarithmic Operations:** Insertion and deletion of elements take 
O(logn) time, where $n is the number of elements in the heap.
* **No Fixed Order (except root):** Elements are not fully sorted; only 
the heap property is maintained.
* **Useful for:** Maintaining order in a dynamic set, finding K-extremes, 
simulations where you always need the "next best" item.

---

#### 2. Monotonic Stack Problems

A **Monotonic Stack** is a stack where the elements are always kept in 
either **strictly increasing** or **strictly decreasing** order (from 
bottom to top). 
When you try to push a new element, you first pop elements from the top of 
the stack that violate this monotonic property.

**How to Identify a Monotonic Stack Problem:**

Look for problems that involve finding the "next greater/smaller element," 
"previous greater/smaller element," or
calculating areas/spans related to elements' relative heights/values within 
an array or sequence. These problems often require efficient lookups for 
elements *to the left or right* that satisfy a certain ordering condition.

* **"Next Greater/Smaller Element" (NGE/NSE):** 
- This is the most common use case. For each element, you need to find the 
first element to its right (or left) that is greater than/smaller than it.
- *Example:* 
    - Next Greater Element I
    - Next Greater Element II (circular array), 
    - Daily Temperatures.

* **"Largest Rectangle in Histogram":** 
- A classic problem where a monotonic stack helps find the nearest smaller 
elements to the left and right for each bar, which define the potential 
width of rectangles.

* **"Trapping Rain Water":** 
- While solvable with two pointers, a monotonic stack provides an alternative 
to find bounding walls.

* **Subarray/Subsequence problems involving ranges and relative ordering:** 
- When the solution depends on the immediate neighbors or elements that are 
"visible" from a certain point.

* **Optimizing Nested Loops for "Next/Previous" problems:** 
- If a brute-force $O(N^2)$ solution for finding NGE/NSE is obvious, a 
monotonic stack is often the $O(N)$ optimization.

**Key Monotonic Stack Characteristics:**

* **Local Extremum / Relative Order:** 
- Helps find nearest elements that satisfy a specific ordering. It's about 
relative order of adjacent or "visible" elements.

* **Single Pass Efficiency:** 
- Often solves problems in a single pass $O(N)$ time because each element is 
pushed and popped at most once.

* **Stack's LIFO Property:** 
- The LIFO nature of the stack naturally helps track relevant candidates for 
"next/previous" elements. When an element is popped, it's because a more 
relevant (monotonic-violating) element has come along, meaning the popped 
element will no longer be the answer for anything to its right (or left).

* **Useful for:** Calculating spans, areas, distances, or finding specific 
neighbors in a sequence where the "monotonic" property is critical.

---

#### Do they look the same?

**They can look similar if you only focus on "finding min/max."**

* **Heap:** 
- Finds the *global* min/max efficiently among a *dynamic set* of elements. It 
doesn't care about the relative position of elements within the input sequence, 
only their values.

* **Monotonic Stack:** 
- Finds *local* min/max properties or specific ordered neighbors within a 
sequence The order of elements in the input sequence matters.

**Think about it this way:**

* **Heap:** 
- Out of all elements I've seen so far (or am managing), give me the smallest 
or largest one, regardless of where it came from in the input."

* **Monotonic Stack:** 
- As I scan through this sequence, for the current element, who is the *next* 
element to my right (or left) that is greater/smaller than me? And who are the 
elements that are no longer relevant because someone 'taller' or 'shorter' came 
along?"

**Example of the distinction:**

* **Problem:** Find the maximum element in a sliding window of size K.
    
    * **Heap Approach:** You could use a max-heap. Add elements to the heap 
    as the window slides. When an element leaves the window, remove it from 
    the heap. The max element is always at the root. (This works, but removal 
    from a heap is $O(log K)$ which can be slow if elements aren't easily 
    referenceable for removal)

    * **Monotonic Queue (Deque) Approach:** This is usually the more optimal 
    solution. A deque (double-ended queue) is used to maintain a *decreasing* 
    sequence of elements (or their indices) within the current window. When a 
    new element comes in, pop smaller elements from the back. When an element 
    goes out of window, pop it from the front if it's the max. The max is always 
    at the front. (takes $O(N)$)

In the sliding window example, both can be applied, but the monotonic queue 
(a variation of monotonic stack logic) provides a better constant-factor $O(N)$ 
solution than a heap's $O(N \log K)$. This highlights that while both deal with 
extremums, the *context* of "locality" or "neighborhood" often points towards 
monotonic stack/queue.


-------------------------------------------------------------------------------------
### Q013 : Understanding Heap with DSA Problems Identification;;

Let's dive into heaps, how to spot problems where they're useful, and then 
walk through the thinking process for LeetCode problem 347, "Top K Frequent 
Elements," without writing any code.

---

#### Understanding Heaps (Min and Max)

A **heap** is a specialized tree-based data structure that satisfies the 
heap property. It's commonly implemented as an array, taking advantage of 
the fact that a complete binary tree can be perfectly mapped to an array.

**Heap Property:**

* **Min-Heap:** For any given node `i`, the value of node `i` is less than 
or equal to the value of its children. This means the smallest element is 
always at the root.
    
    * Think of it like a priority queue where the *lowest* value has the 
    highest priority.

* **Max-Heap:** For any given node `i`, the value of node `i` is greater 
than or equal to the value of its children. This means the largest element 
is always at the root.

    * Think of it like a priority queue where the *highest* value has the 
    highest priority.

**Key Characteristics & Operations:**

* **Complete Binary Tree:** 
- All levels of the tree are fully filled, except possibly the last level, 
which is filled from left to right. This allows for efficient array 
representation.

* **Root Element:** 
- The root (first element in the array representation) always contains the 
minimum element in a min-heap, or the maximum element in a max-heap.

* **`heapify` (Build Heap):** 
- Rearranging an arbitrary array into a heap.
- Time Complexity: o(n) time

* **`insert` (Push):** 
- Add a new element to the heap while maintaining the heap property. 
- Time Complexity: o(logn)

* **`extract_min/max` (Pop):** 
- Remove the root element (min/max) and reorganize the heap to maintain the 
heap property. 
- Time Complexity: o(logn)

* **`peek_min/max`:** 
- Look at the root element without removing it. 
- Time Complexity: o(1)

**Analogy:**
Think of a heap like a very organized line at a theme park, but instead of 
first-come, first-served, it's "smallest value first" (min-heap) or "largest 
value first" (max-heap). 
When someone gets on the ride (extracted), the next smallest/largest person 
immediately moves to the front. When someone new joins the line (inserted), 
they find their proper place quickly.

---

#### How to Identify DSA Problems Related to Heaps

Heaps are primarily used when you need to efficiently find or retrieve the 
**kth smallest/largest element**, the **smallest/largest element repeatedly**, 
or maintain a **dynamically ordered collection** where only the extreme 
values matter.

Here are the "signals" that often point to a heap solution:

1.  **"Top K" or "Kth Smallest/Largest"**: 
- This is the strongest indicator. When a problem asks for the *k* most 
frequent, *k* largest, *k* smallest, *k* longest, etc., a heap is almost 
always the optimal approach.
- Examples: 
    - Top K Frequent Elements 
    - Kth Largest Element in an Array 
    - K Closest Points to Origin.

2.  **"Median in a Stream" / "Data Stream"**: 
- When you need to maintain an ordered collection and query the median 
or some extreme value as elements are added one by one. Two heaps (one 
min-heap, one max-heap) are often used here.
- Example: 
    - Find Median from Data Stream.

3.  **"Priority Queue" Semantics**: 
- If the problem description naturally implies a priority queue – elements 
need to be processed in a specific order (e.g., shortest path first, highest 
profit first, earliest deadline first) – a heap is the underlying data 
structure for a priority queue.
- Examples: 
    - Dijkstra's Algorithm (shortest path)
    - Huffman Coding, Event Scheduling.

4.  **Maintaining Order in a Limited Size**: 
- When you only care about a fixed number of the "best" or "worst" elements, 
and the total number of elements could be very large. A min-heap of size `k` 
(to find largest) or a max-heap of size `k` (to find smallest) is perfect.

5.  **Smallest/Largest Element Repeatedly**: If you need to repeatedly extract 
the minimum or maximum element from a collection and then possibly re-insert 
modified elements.
- Example: 
    - Merge K Sorted Lists/Arrays (repeatedly extract smallest from K sources).

**General Rule of Thumb:** If you find yourself thinking, "I need the *X* best 
or worst items from a large collection, but I don't need to sort the whole 
thing," then a heap is your friend.

---

#### Approaching LeetCode 347: Top K Frequent Elements

**Problem Statement:** Given an integer array `nums` and an integer `k`, 
return the `k` most frequent elements. You may return the answer in any 
order.

Let's walk through the thought process:

**1. Brute-Force Approach:**

* **Idea:** Count frequencies of all numbers. Then, sort based on these frequencies. 
Finally, pick the top `k`.

* **Steps:**
    1.  Create a way to store counts. A hash map (dictionary) `frequency_map` 
    would be perfect: `number -> count`.
    2.  Iterate through `nums`. For each number, increment its count in 
    `frequency_map`.
    3.  Once all counts are gathered, you have `number -> count` pairs. You 
    need to 
    sort these pairs. How? Convert the `frequency_map` items into a list of 
    tuples `[(number1, count1), (number2, count2), ...]`.
    4.  Sort this list of tuples. The sorting key would be the `count` (the 
    second element of the tuple), in descending order.
    5.  After sorting, take the first `k` numbers from the sorted list.

* **Example `nums = [1,1,1,2,2,3], k = 2`:**
    1.  `frequency_map = {1: 3, 2: 2, 3: 1}`
    2.  Convert to list of tuples: `[(1, 3), (2, 2), (3, 1)]`
    3.  Sort by count (descending): `[(1, 3), (2, 2), (3, 1)]` (already sorted 
    in this simple case).
    4.  Take top `k=2`: `[1, 2]`

* **Analysis:**
    * **Counting:** $O(N)$ to iterate through `nums` and update hash map.
    * **Sorting:** If there are `M` unique numbers, sorting `M` pairs takes O(MxlogM). 
    In the worst case, `M` can be `N` (all numbers unique). So, O(NxlogN).
    * **Overall Time:** O(Nxlog N).
    * **Space:** O(M) for the hash map and the list of tuples. In worst case, O(N).

* **Verdict:** This is a correct approach but might not be optimal if `N` is very large 
and `k` is relatively small. The O(Nxlog N) from sorting is the bottleneck.

**2. Optimized Approach (without Heap, using Bucket Sort idea or Quickselect idea):**

* **Idea:** Can we avoid a full sort? If we only care about counts, maybe 
we can group numbers by their counts.

* **Steps:**
    1.  **Count Frequencies:** (Same as brute-force) Use a `frequency_map` to 
    get `number -> count` for all elements. O(N) time.
    2.  **Bucket by Frequency:** Create an array of lists, where the index 
    represents a frequency, and the list at that index contains all numbers 
    that have that frequency.
        * `buckets = [[] for _ in range(N + 1)]` (indices 0 to N, max frequency is N)
        * Iterate through `frequency_map.items()`: 
            `for num, count in frequency_map.items(): buckets[count].append(num)`
        * Example `frequency_map = {1: 3, 2: 2, 3: 1}`:
            * `buckets[1] = [3]`
            * `buckets[2] = [2]`
            * `buckets[3] = [1]`
    3.  **Collect Top K:** Iterate through the `buckets` array from the 
    highest frequency index down to 1. Add numbers to your `result` list 
    until you have `k` elements.
        * `result = []`
        * `for count_idx in range(N, 0, -1):`
        * `for num in buckets[count_idx]:`
        * `result.append(num)`
        * `if len(result) == k: return result`

* **Analysis:**
    * **Counting:** O(N).
    * **Bucketing:** O(M) to iterate through unique numbers and place them 
    in buckets.
    * **Collecting:** In the worst case, you might iterate through many buckets 
    to find `k` elements, but each element is placed in a bucket once. Total 
    elements across all buckets is `M`. So $O(M)$.
    * **Overall Time:** $O(N)$ (linear time!). This is because we avoid a full 
    sort. The maximum frequency is `N`, so `buckets` array size is `N+1`.
    * **Space:** $O(N)$ for the `frequency_map` and the `buckets` array.

* **Verdict:** This is an optimal solution. It achieves $O(N)$ time complexity.

**3. Optimized Approach (Using a Min-Heap):**

* **Idea:** We want the *K largest* frequencies. A min-heap is counter-intuitive 
but perfect for this! We maintain a min-heap of size `k`. If we encounter a pair 
`(number, frequency)` with a frequency *greater* than the smallest frequency in 
our heap (i.e., the heap's root), we remove the smallest and add the new, larger 
one. This way, the heap always contains the `k` largest frequencies seen so far.

* **Steps:**
    1.  **Count Frequencies:** (Same as brute-force) Use a `frequency_map` to get 
    `number -> count` for all elements. $O(N)$ time.
    2.  **Initialize a Min-Heap:** Create an empty min-heap. We'll store 
    `(frequency, number)` tuples in the heap. Python's `heapq` module is a min-heap.
    3.  **Populate the Heap:**
        * Iterate through each `(num, count)` pair in `frequency_map`.
        * **If the heap's size is less than `k`:** Simply push `(count, num)` 
        onto the heap.
        * **If the heap's size is equal to `k`:**
            * Check the smallest element in the heap (the root). Its frequency 
            is `heap[0][0]`.
            * If `count` is greater than `heap[0][0]` (smallest frequency 
            currently in the heap):
                * Pop the root element (`heapq.heappop`).
                * Push the new element `(count, num)` onto the heap (`heapq.heappush`).
            * Else (if `count` is less than or equal to `heap[0][0]`): 
            Do nothing. This number's frequency is not among the top `k`.
    4.  **Extract Results:** Once all `frequency_map` items are processed, the 
    heap will contain the `k` most frequent elements (or fewer, if there are less 
    than `k` unique elements). Extract the numbers from the heap.

* **Example `nums = [1,1,1,2,2,3], k = 2`:**
    1.  `frequency_map = {1: 3, 2: 2, 3: 1}`
    2.  `min_heap = []`
    3.  **Process `(1, 3)`:** `heap` size < 2. 
    eg, `heapq.heappush(min_heap, (3, 1))`. `min_heap = [(3, 1)]`
    4.  **Process `(2, 2)`:** `heap` size < 2. (heap property maintains min at root)
    eg, `heapq.heappush(min_heap, (2, 2))`. `min_heap = [(2, 2), (3, 1)]` .
    5.  **Process `(3, 1)`:** `heap` size == 2. `count = 1`. `min_heap[0][0] = 2`. 
    Is `1 > 2`? No. Do nothing. `min_heap` remains `[(2, 2), (3, 1)]`
    6.  **End of processing.**
    7.  Extract numbers from heap: `[2, 1]` (order might vary based on ties, but 
    `1` and `2` are the elements).

* **Analysis:**
    * **Counting:** O(N)
    * **Heap Operations:** For each of the `M` unique numbers, we perform at 
    most one `push` and one `pop` operation. Each heap operation takes $O(log k)$ 
    time (because the heap size is capped at `k`). So, O(Mxlog k). 
    In the worst case, `M` can be `N`. So, O(Nxlog k).
    * **Overall Time:** O(N + Nxlog k) which simplifies to O(Nxlog k).
    * **Space:** $O(M)$ for the `frequency_map` and $O(k)$ for the min-heap. 
    So, O(N + k), which simplifies to $O(N)$ in the worst case where `k` can be `N`.

* **Verdict:** This is a very common and efficient solution, especially
when `k` is much smaller than `N`. $O(N \log k)$ is often better than 
O(Nxlog N) (from full sort) and a good general-purpose solution.


-------------------------------------------------------------------------------------
### Q012 : Anagram Array and Strings in DSA;;

Let's delve into Anagrams within the context of Data Structures and Algorithms 
(DSA). This is a common and fundamental concept that frequently appears in 
interview problems.

#### What are Anagrams?

Anagram is a word or phrase formed by rearranging the letters of a different 
word or phrase, typically using all the original letters exactly once. 

The key here is **rearrangement** and **using all letters exactly once**.

**Examples:**
* "listen" and "silent" are anagrams.
* "Debit card" and "Bad credit" are anagrams.
* "aab" and "aba" are anagrams.
* "cat" and "act" are anagrams.
* "hello" and "hellos" are *not* anagrams (different lengths, 's' missing).
* "apple" and "apply" are *not* anagrams (different letters).

#### Anagrams in DSA: The Core Idea

In DSA problems, the concept of anagrams almost always boils down to one 
fundamental property:

Two strings (or arrays of characters/elements) are anagrams of each other 
if and only if they have the *same characters with the same frequencies* 
(counts) of each character.

The order of characters doesn't matter, only their composition.

#### Common Anagram Problems in DSA

You'll typically encounter anagram problems in these forms:

1.  Check if two given strings are anagrams.
2.  Find all anagrams of a pattern string within a larger text string.
3.  Group a list of strings into groups of anagrams.
4.  Find if a string contains a permutation (anagram) of another string as 
a substring.

#### How to Detect Anagrams (The DSA Techniques)

Based on the core idea of character frequencies, here are the most common 
and efficient techniques:

#### 1. Using a Hash Map (or Dictionary/Frequency Array) - BEST

This is the go-to method for checking anagrams and is very flexible.

**Concept:** Count the occurrences of each character in the first string. 
Then, for the second string, decrement the counts. If all counts end up at 
zero, they are anagrams.

**Steps to check if `s1` and `s2` are anagrams:**

1.  **Pre-check:** If `len(s1) != len(s2)`, they cannot be anagrams. 
Return `false`.

2.  **Initialize a frequency map:** Create a hash map (or an array of size 26 
for lowercase English letters, 128 for ASCII, 256 for extended ASCII, etc.) 
initialized to zeros.

3.  **Populate for `s1`:** Iterate through `s1`. For each character, increment 
its count in the map. For eg, `s1 = "listen"`
    * `{'l': 1, 'i': 1, 's': 1, 't': 1, 'e': 1, 'n': 1}`

4.  **Decrement for `s2`:** Iterate through `s2`. For each character:
    * Decrement its count in the map.
    * If a character is encountered that is *not* in the map, or its count 
    drops below zero, then `s1` and `s2` are not anagrams. Return `false`.
    * Example: `s2 = "silent"`
        * `s`: {'s': 0, ...}
        * `i`: {'i': 0, ...}
        * ... and so on.

5.  **Final Check:** After iterating through `s2`, if all counts in the map 
are zero, then `s1` and `s2` are anagrams. Return `true`. 

(You don't strictly need to iterate through the map if you caught negative 
counts in step 4, but it's a good mental model).

**Time Complexity:** O(L) where $L is the length of the strings because you 
iterate through each string once.

**Space Complexity:** O(C) where $C is the size of the character set 
(e.g., 26 for English alphabet).

#### 2. Sorting - Simpler for Two Strings, Less Flexible for Groups

**Concept:** If two strings are anagrams, then sorting their characters 
alphabetically will result in identical strings.

**Steps to check if `s1` and `s2` are anagrams:**

1.  **Pre-check:** If `len(s1) != len(s2)`, return `false`.

2.  **Sort:** Convert both strings to character arrays (or lists), sort them, 
and convert them back to strings (or compare the sorted arrays directly).
    * Example:
        * `s1 = "listen"` -> `['e', 'i', 'l', 'n', 's', 't']`
        * `s2 = "silent"` -> `['e', 'i', 'l', 'n', 's', 't']`

3.  **Compare:** If the sorted strings/arrays are identical, they are anagrams.

**Time Complexity:** O(nlogn) due to sorting where $n is the length of the strings 
This is generally slower than the hash map approach for typical string lengths, 
but can be simpler to implement quickly.

**Space Complexity:** O(L) or O(1) depending on whether the sorting algorithm uses 
extra space or sorts in-place.

#### 3. Prime Product (A Niche Trick)

**Concept:** Assign a unique prime number to each letter of the alphabet. Multiply 
the prime numbers corresponding to the letters in a word. If two words are anagrams, 
their prime products will be the same.

**Example:**

* a=2, b=3, c=5, d=7, e=11...
* "cat" -> 5 * 2 * 17 = 170
* "act" -> 2 * 5 * 17 = 170

**Pros:** Potentially very fast for comparison if hashes are pre-computed.

**Cons:**

* **Collision risk:** If numbers are large, you might hit integer overflow issues 
before you've multiplied all primes.
* **Limited character set:** Only practical for small, fixed alphabets.
* **Not common:** Less flexible and less frequently seen in general DSA problems 
compared to hash maps.

#### Anagram Array Problems (Example: Group Anagrams)

This is where the "Array of Strings" comes into play. You're given `list[str]` and 
need to group them.

**Problem:** `strs = ["eat", "tea", "tan", "ate", "nat", "bat"]`

**Output:** `[["eat","tea","ate"], ["tan","nat"], ["bat"]]`

**Solution Idea:**

1.  **Canonical Form:** For each string, transform it into a "canonical" form such 
that all its anagrams will transform into the *same* canonical form. The easiest 
canonical form is the **sorted version of the string**.
    * "eat" -> "aet"
    * "tea" -> "aet"
    * "tan" -> "ant"
    * "ate" -> "aet"
    * "nat" -> "ant"
    * "bat" -> "abt"

2.  **Group using a Hash Map:** Use a hash map where:
    * **Keys:** The canonical form of a string (e.g., "aet").
    * **Values:** List of all original strings that transform into that canonical form.

3.  **Iterate and Populate:**
    * For each `s` in `strs`:
        * `canonical_s = "".join(sorted(s))`
        * Add `s` to the list associated with `canonical_s` in your hash map.

4.  **Extract Results:** The values of your hash map will be your groups of anagrams.

**Example Walkthrough:**

* `strs = ["eat", "tea", "tan", "ate", "nat", "bat"]`
* `anagram_groups = {}`

1.  `s = "eat"`: `sorted("eat")` -> "aet". 
`anagram_groups = {"aet": ["eat"]}`

2.  `s = "tea"`: `sorted("tea")` -> "aet". 
`anagram_groups = {"aet": ["eat", "tea"]}`

3.  `s = "tan"`: `sorted("tan")` -> "ant". 
`anagram_groups = {"aet": ["eat", "tea"], "ant": ["tan"]}`

4.  `s = "ate"`: `sorted("ate")` -> "aet". 
`anagram_groups = {"aet": ["eat", "tea", "ate"], "ant": ["tan"]}`

5.  `s = "nat"`: `sorted("nat")` -> "ant". 
`anagram_groups = {"aet": ["eat", "tea", "ate"], "ant": ["tan", "nat"]}`

... so on


Final result is `anagram_groups.values()`.

**Alternative for Canonical Form (Frequency Tuple/String):**
Instead of sorting, you can use a frequency array/map to create a canonical 
representation.

For eg, "eat", frequency map: `{'a':1, 'e':1, 't':1}`. You can represent this 
as a tuple `(1,1,0,0,1,...)` for a-z counts or a string like `"a1e1t1"`. This 
avoids sorting cost.

For English lowercase, a common way is `tuple(counts)` where `counts` is a 
length-26 array.

```python
# Example for frequency tuple canonical form
def get_char_counts(s):
    counts = [0] * 26 # For 'a' through 'z'
    for char in s:
        print(f"{char=}, {char=}: {ord(char)}")
        print(f"{char=}, a: {ord('a')}")
        print(f"{char=}, diff: {ord(char) - ord('a')}")
        counts[ord(char) - ord('a')] += 1

    return tuple(counts) # Convert to tuple to make it hashable for dict key

# Then, in the grouping problem:
# canonical_form = get_char_counts(s)
# my_map[canonical_form].append(s)

# Output:
# char='e', char='e': 101
# char='e', a: 97
# char='e', diff: 4
# xs=(0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

```
This frequency counting approach for the canonical form has o(n) complexity 
(string length) instead of $O(nlogn) for sorting, making it more efficient for
longer strings.


#### Key Takeaways for Anagrams in DSA:

* **Frequency is King:** Anagrams are all about character frequencies.
* **Hash Maps/Frequency Arrays:** Your primary tool for tracking character 
counts efficiently ($O(1)$ average access).
* **Sorting:** A simpler alternative for comparing two strings, but less 
efficient and flexible for groups.

* **Canonical Form:** The crucial idea for grouping anagrams. Transform every
string into a unique representation that all its anagrams share.

* **Edge Cases:** Always consider empty strings, single-character strings, and 
strings with non-alphabetic characters (and whether they should be considered 
in the anagram check).


-------------------------------------------------------------------------------------
### Q011 : BitWise Right Shift Operator Dividing Usecase;;

Let's dive into **bitwise right shift (`>>`)** — the opposite of what you 
just saw with left shift.

---

#### What does `>>` do?

Bitwise right shift `x >> y` shifts the bits of `x` to the right by `y` 
positions.

This is equivalent to:

> **Integer division** of `x` by `2^y`.

---

#### Example: `10 >> 1`

```text
Decimal: 10
Binary:  1010
```

Now, shift all bits **right by 1**:

```text
 1010   (10)
>> 1
 ----
 0101   (5)
```

So:

```python
10 >> 1 == 5 → 10 // 2^1 = 5
```

---

#### Why is this like dividing by 2?

Each bit position represents a **power of 2**.

Right shifting a binary number moves each bit **down one power**, effectively 
dividing the value by 2 for each shift.

```python
10 >> 1 == 10 // 2 == 5
10 >> 2 == 10 // 4 == 2
```

Only the **integer part** is kept. No decimals.

---

#### Real-World Use Cases of Right Shift (`>>`)

1. **Fast division by powers of 2** (where speed matters)
2. **Bitmasking or decoding packed data**
3. **Binary search logic**
4. **Efficient calculations in embedded systems, low-level apps, or game engines**

---

#### Comparison Summary

| Operation | Symbol | Meaning                   | Example       |
| --------- | ------ | ------------------------- | ------------- |
| Left      | `<<`   | Multiply by 2^n           | `5 << 1 = 10` |
| Right     | `>>`   | Divide by 2^n (floor div) | `10 >> 1 = 5` |


-------------------------------------------------------------------------------------
### Q010 : BitWise Left Shift Operator Multiplying Usecase;;

Let's break it down and explore why left shifting (`<<`) a number is 
equivalent to multiplying by powers of 2**i

---

#### Binary of 5

`5` in binary = `0101`

Now apply:

#### Left Shift: `5 << 1`

Shifting all bits to the **left by 1 place** gives:

```
    0101   (5)
    << 1
----------------
    1010   (10)
```

**Result** = `10` in decimal

---

#### Why is this like `2^y`?

Left shifting by `y` places is **multiplying the number by `2^y`**.

So:

```python
5 << 1 == 5 * (2^1) == 10
5 << 2 == 5 * (2^2) == 20
5 << 3 == 5 * (2^3) == 40
```

---

#### Reasoning (Bitwise Math)

Each binary **digit (bit)** represents an increasing power of 2:

```
Binary:   0 1 0 1  (5)
Powers:   8 4 2 1
Value :   0+4+0+1 = 5
```

Now if you **shift left**, all bits move to higher powers of 2. So:

* The `1` at `2^2` becomes `2^3`
* The `1` at `2^0` becomes `2^1`

That’s why it **doubles the number** with each shift.

---

#### Visual Summary

| Decimal | Binary | `<< 1` Result | Equivalent |
| ------- | ------ | ------------- | ---------- |
| 5       | 0101   | 1010 (10)     | 5 × 2¹     |
| 3       | 0011   | 0110 (6)      | 3 × 2¹     |
| 6       | 0110   | 1100 (12)     | 6 × 2¹     |

---

So, when you do `a << y`, it's exactly `a * (2^y)`.


-------------------------------------------------------------------------------------
### Q009 : Bitwise XOR Operator Swapping Usecase;;

Classic example of **swapping two variables using XOR** — a neat trick that 
doesn't require a third temporary variable:

---

#### Swap Two Numbers Using XOR

```python
# Initial values
a = 5
b = 7

print("Before swap:")
print(f"a = {a}, b = {b}")

# XOR Swap Logic
a = a ^ b
b = a ^ b  # (a ^ b) ^ b = a
a = a ^ b  # (a ^ b) ^ a = b

print("\nAfter swap:")
print(f"a = {a}, b = {b}")
```

---

#### Why It Works?

Let's say:

* `a = 5` → `0101` in binary
* `b = 7` → `0111` in binary

Step-by-step:

1. `a = a ^ b` → stores the XOR of a and b in $a whch is 2
2. `b = a ^ b` → retrieves original `a`
3. `a = a ^ b` → retrieves original `b`

---

#### Caution

* This only works **safely** with **primitive data types (ints)**.
* It can be confusing in real code, so it's more of a cool trick or interview 
concept than best practice in production.


-------------------------------------------------------------------------------------
### Q008 : Boyer Moorie Algorithm In-Depth;;

Boyer-Moore Majority algorithm is specifically designed to find the majority 
element in an array, which is an element that appears **more than $N/2$ times** 
(where $N$ is the array's length).

#### The Core Idea: Cancellation / "Voting"

Imagine you have a group of people, and each person holds a sign with a number on 
it. You want to find out if there's a number that appears on more than half the 
signs.

The Boyer-Moore algorithm is like a "vote cancellation" process. It relies on the
simple fact that if an element *is* a majority element, it will appear so frequently 
that it can "cancel out" all other distinct elements in the array, and still be left 
standing.

#### The Analogy: The Duel (or Political Debate with Cancelling Votes)

Let's use a "Duel" analogy:

You have a group of people, each representing a "vote" for a particular "candidate" 
(the number they hold). You want to find the candidate with the *absolute majority*.

1.  **Pick your first "champion":** You look at the first person in the line. Let's 
say their sign says '5'. You declare '5' as your current "champion" and give them 1 
point.
    * `current_champion = 5`
    * `champion_score = 1`

2.  **Go through the line, one by one:**

    * If the next person supports your `current_champion` (same number on their sign) 
    then your champion gains a point.
        * `champion_score += 1`

    * If the next person supports a *different* candidate (different number) then your 
    champion loses a point. Think of it as their votes "cancelling out" one opposing vote.
        * `champion_score -= 1`

    * **Crucial point:** If your `champion_score` drops to zero then Your current champion 
    has been "defeated" or "neutralized." You *forget* them. Now, you pick the next person 
    you see as your new `current_champion` and give them 1 point. This is like switching 
    allegiance to a new potential majority candidate because your previous one couldn't 
    sustain their lead.

3.  **After going through everyone:**
    You'll be left with a `current_champion` and their `champion_score` (which must be $>0$). 
    This `current_champion` is your **potential majority element**.


#### Why is this only a "potential" majority?

Because the algorithm *always* produces a candidate, even if there isn't a true majority element.

Consider `[1, 2, 3]`.
* Pick 1, score 1.
* See 2, score 0, switch to 2, score 1.
* See 3, score 0, switch to 3, score 1.
Candidate is 3. But 3 is not a majority element.

So, after the first pass, you need a **second verification pass**.


#### The Two Phases of the Algorithm (Formal Steps)

**Phase 1: Finding the Candidate (The "Voting" / "Duel" Process)**

1.  **Initialize:**
    * `candidate = None` (or any placeholder, effectively no champion initially)
    * `count = 0` (your champion's score)

2.  **Iterate through each `number` in the array `nums`:**
    * **If `count` is 0:**
        * This means your previous champion was "defeated" or you're just starting.
        * Set `candidate = number` (The current number becomes your new champion).
        * Set `count = 1` (Your new champion starts with 1 point).
    * **Else if `number` is equal to `candidate`:**
        * The current number supports your champion.
        * Increment `count` by 1.
    * **Else (if `number` is not equal to `candidate`):**
        * The current number opposes your champion.
        * Decrement `count` by 1.

**NOTE:** At the end of Phase 1, `candidate` will hold the value of a number that 
might be the majority element.

---

**Phase 2: Verification (The "Counting the Actual Votes" Process)**

This phase is **absolutely crucial**. The first phase only guarantees that if a 
majority element exists, it will be the `candidate` at the end. It *does not* 
guarantee that the `candidate` *is* a majority element.

1.  **Initialize `actual_occurrences = 0`**

2.  **Iterate through each `number` in the array `nums` *again*:**
    * **If `number` is equal to `candidate`:**
        * Increment `actual_occurrences` by 1.

3.  **Final Check:**
    * **If `actual_occurrences > len(nums) / 2`:**
        * Then `candidate` is indeed the majority element.
    * **Else:**
        * There is no majority element in the array.

#### Why Does It Work So Efficiently?

The magic lies in the cancellation. If a number `M` appears more than $N/2$ times, 
then even if every non-`M` number cancels out an `M`, there will *always* be `M`s 
left over.

Imagine $N$ items. If `M` appears $X$ times, and other elements appear $Y$ times. 
We know $X > N/2$. When we do cancellations, each non-`M` element cancels out one 
`M` (if `M` is the current candidate). The maximum number of `M`s that can be 
cancelled is $Y$.

Since $X > Y$ (because $X > N/2$ and $Y < N/2$), there will always be `M`s 
remaining, ensuring that `M`'s `count` will never permanently drop to zero and 
allow another element to become the candidate and stay there until the end without 
`M` taking over again.

**REMARK:** It doesn't need to store all elements or their counts, making it o(1) space.

#### Example Walkthrough: `nums = [2, 2, 1, 1, 1, 2, 2]` ($N=7$)

**Phase 1: Finding the Candidate**

| Current `number` | `candidate` | `count` | Explanation                                   |
| :--------------- | :---------- | :------ | :---------------------------------------------|
| Initial          | `None`      | `0`     | Start state                                   |
| `2`              | `2`         | `1`     | `count` was 0, so '2' becomes new candidate.  |
| `2`              | `2`         | `2`     | `number` == `candidate`, increment count.     |
| `1`              | `2`         | `1`     | `number` != `candidate`, decrement count.     |
| `1`              | `1`         | `1`     | `count` was 0, so '1' becomes new candidate.  |
| `1`              | `1`         | `2`     | `number` == `candidate`, increment count.     |
| `2`              | `1`         | `1`     | `number` != `candidate`, decrement count.     |
| `2`              | `2`         | `1`     | `count` was 0, so '2' becomes new candidate.  |

**End of Phase 1:** `candidate = 2`, `count = 1`.

---

**Phase 2: Verification**

* `candidate = 2`
* `actual_occurrences = 0`

Iterate through `nums = [2, 2, 1, 1, 1, 2, 2]` again:

* `number = 2`: `2 == candidate`. `actual_occurrences = 1`.
* `number = 2`: `2 == candidate`. `actual_occurrences = 2`.
* `number = 1`: `1 != candidate`. (Do nothing)
* `number = 1`: `1 != candidate`. (Do nothing)
* `number = 1`: `1 != candidate`. (Do nothing)
* `number = 2`: `2 == candidate`. `actual_occurrences = 3`.
* `number = 2`: `2 == candidate`. `actual_occurrences = 4`.

**Final Check:**
* `actual_occurrences = 4`
* `len(nums) / 2 = 7 / 2 = 3.5`
* Is `4 > 3.5`? Yes.

**Conclusion:** The majority element is `2`.

---

#### Example without a Majority Element: `nums = [1, 2, 3, 1, 2]` ($N=5$)

**Phase 1: Finding the Candidate**

| Current `number` | `candidate` | `count` |
| :--------------- | :---------- | :------ |
| Initial          | `None`      | `0`     |
| `1`              | `1`         | `1`     |
| `2`              | `1`         | `0`     |
| `3`              | `3`         | `1`     |
| `1`              | `3`         | `0`     |
| `2`              | `2`         | `1`     |

**End of Phase 1:** `candidate = 2`, `count = 1`.

---

**Phase 2: Verification**

* `candidate = 2`
* `actual_occurrences = 0`

Iterate through `nums = [1, 2, 3, 1, 2]` again:

* `number = 1`: `1 != candidate`.
* `number = 2`: `2 == candidate`. `actual_occurrences = 1`.
* `number = 3`: `3 != candidate`.
* `number = 1`: `1 != candidate`.
* `number = 2`: `2 == candidate`. `actual_occurrences = 2`.

**Final Check:**
* `actual_occurrences = 2`
* `len(nums) / 2 = 5 / 2 = 2.5`
* Is `2 > 2.5`? No.

**Conclusion:** There is no majority element in the array.

This analogy and detailed walkthrough should give you a solid grasp of how the 
Boyer-Moore Majority Vote Algorithm works, its underlying logic, and why it's 
so efficient!


-------------------------------------------------------------------------------------
### Q007 : Monotonic Stacks Algorithms In-Depth;;

#### Monotonic Stack: The Core Concept

A monotonic stack is a stack data structure that maintains elements in either 
strictly increasing or strictly decreasing order. This means:

* **Monotonically Increasing Stack:** 
Elements pushed onto the stack are always greater than or equal to the element 
below them. If you try to push a smaller element, you pop elements from the top 
until the condition is met.

* **Monotonically Decreasing Stack:** 
Elements pushed onto the stack are always less than or equal to the element below 
them. If you try to push a larger element, you pop elements from the top until 
the condition is met.

The key insight is that when you push a new element onto a monotonic stack, you 
effectively process all elements on the stack that violate the monotonic property 
*with respect to the new element*. This processing is what makes monotonic stacks 
so powerful for certain types of problems.

#### Why Monotonic Stacks are Useful:

Monotonic stacks are particularly effective for problems where you need to find the:

* **Next Greater/Smaller Element:** 
For each element, find the first element to its right (or left) that is greater than 
or smaller than it.

* **Previous Greater/Smaller Element:** 
For each element, find the first element to its left (or right) that is greater than 
or smaller than it.

* **Subarray/Subsequence Problems:** 
Problems involving finding the maximum/minimum area of rectangles, counting subarrays 
with specific properties, etc., where the "monotonic" property helps in efficiently 
determining boundaries or contributions.

#### Common Patterns/Template:

While there are variations, a common pattern for problems involving next greater or 
smaller elements to the *right* goes like this:

1.  Initialize an empty stack.
2.  Iterate through the input array from left to right.
3.  For each element `num`:
    * While the stack is not empty AND `num` violates the monotonic property with 
    stack.top()
    * Pop `stack.top()`. This popped element has `num` as its "next greater/smaller" 
    element. Process this relationship (e.g., store it in a result array/map).
    * Push `num` onto the stack.

If you need to find the "previous greater/smaller" elements to the *left*, you can 
often iterate from right to left.

#### Multi-Usecases of Monotonic Stack

Let's explore several common use cases to solidify your understanding.

**Usecase 1: Next Greater Element (to the Right)**

**Problem:** For each element in an array, find the first element to its right that is 
greater than it. If no such element exists, store -1.

**Example:** `nums = [2, 1, 5, 4, 3]`

**Monotonic Stack Type:** Decreasing. We want to find a *greater* element. When we 
encounter an element `x` that is greater than `stack.top()`, it means `x` is the next 
greater element for `stack.top()`.

**Walkthrough:**

1.  `stack = []`, `result = {}` (or an array initialized with -1)

2.  **`num = 2`:**
    * Stack is empty. Push 2. `stack = [2]`

3.  **`num = 1`:**
    * `stack.top() = 2`. `1 < 2`. Monotonic property (decreasing) holds. Push 1. 
    stack = [2, 1]

4.  **`num = 5`:**
    * `stack.top() = 1`. `5 > 1`. Pop 1. `result[1] = 5`. `stack = [2]`
    * `stack.top() = 2`. `5 > 2`. Pop 2. `result[2] = 5`. `stack = []`
    * Stack is empty. Push 5. `stack = [5]`

5.  **`num = 4`:**
    * `stack.top() = 5`. `4 < 5`. Monotonic property holds. Push 4. `stack = [5, 4]`

6.  **`num = 3`:**
    * `stack.top() = 4`. `3 < 4`. Monotonic property holds. Push 3. `stack = [5, 4, 3]`

**End of iteration:**
* `stack = [5, 4, 3]`
* Elements remaining in the stack have no next greater element to their right in the 
original array. `result[5] = -1`, `result[4] = -1`, `result[3] = -1`.

**Final Result (for original elements):**
* 2 -> 5
* 1 -> 5
* 5 -> -1
* 4 -> -1
* 3 -> -1

**Usecase 2: Next Smaller Element (to the Right)**

**Problem:** For each element in an array, find the first element to its right that is 
smaller than it. If no such element exists, store -1.

**Example:** `nums = [4, 2, 5, 1, 3]`

**Monotonic Stack Type:** Increasing. We want to find a *smaller* element. When we 
encounter an element `x` that is smaller than `stack.top()`, it means `x` is the next 
smaller element for `stack.top()`.

**Walkthrough:**

1.  `stack = []`, `result = {}`

2.  **`num = 4`:** Push 4. `stack = [4]`

3.  **`num = 2`:**
    * `stack.top() = 4`. `2 < 4`. Pop 4. `result[4] = 2`. `stack = []`
    * Stack empty. Push 2. `stack = [2]`

4.  **`num = 5`:**
    * `stack.top() = 2`. `5 > 2`. Monotonic property holds. Push 5. `stack = [2, 5]`

5.  **`num = 1`:**
    * `stack.top() = 5`. `1 < 5`. Pop 5. `result[5] = 1`. `stack = [2]`
    * `stack.top() = 2`. `1 < 2`. Pop 2. `result[2] = 1`. `stack = []`
    * Stack empty. Push 1. `stack = [1]`

6.  **`num = 3`:**
    * `stack.top() = 1`. `3 > 1`. Monotonic property holds. Push 3. `stack = [1, 3]`

**End of iteration:**
* `stack = [1, 3]`
* `result[1] = -1`, `result[3] = -1`

**Final Result:**
* 4 -> 2
* 2 -> 1
* 5 -> 1
* 1 -> -1
* 3 -> -1

**Usecase 3: Previous Greater Element (to the Left)**

**Problem:** For each element in an array, find the first element to its left that is 
greater than it. If no such element exists, store -1.

**Example:** `nums = [2, 1, 5, 4, 3]`

**Monotonic Stack Type:** Decreasing. We iterate from *left to right*. When we push 
an element, it means all elements already on the stack are to its left. If we find 
an element `x` that is greater than our current `num`, that `x` is the previous 
greater element.

**Walkthrough:**

1.  `stack = []`, `result = []` (indexed with original indices)

2.  **`num = 2` (index 0):**
    * Stack empty. `result[0] = -1`. Push 2. `stack = [2]`

3.  **`num = 1` (index 1):**
    * `stack.top() = 2`. `1 < 2`. `result[1] = 2`. Push 1. `stack = [2, 1]`

4.  **`num = 5` (index 2):**
    * `stack.top() = 1`. `5 > 1`. Pop 1. `stack = [2]`
    * `stack.top() = 2`. `5 > 2`. Pop 2. `stack = []`
    * Stack empty. `result[2] = -1`. Push 5. `stack = [5]`

5.  **`num = 4` (index 3):**
    * `stack.top() = 5`. `4 < 5`. `result[3] = 5`. Push 4. `stack = [5, 4]`

6.  **`num = 3` (index 4):**
    * `stack.top() = 4`. `3 < 4`. `result[4] = 4`. Push 3. `stack = [5, 4, 3]`

**Final Result:**
* For 2 (index 0): -1
* For 1 (index 1): 2
* For 5 (index 2): -1
* For 4 (index 3): 5
* For 3 (index 4): 4

**Note:** For "previous" elements, often you're looking for the *first* element that 
satisfies the condition *to the left*. So, when `stack.top()` fulfills the condition, 
that's your answer.

**Usecase 4: Largest Rectangle in Histogram**

**Problem:** Given an array of integers `heights` representing the histogram's bar 
height where the width of each bar is 1, find the area of the largest rectangle in 
the histogram.

**Monotonic Stack Type:** Increasing. We want to find the range where a bar is the 
*shortest* (or tallest, depending on perspective) in a continuous sub-array. When 
we encounter a bar shorter than `stack.top()`, it means `stack.top()` can extend 
its height to the left up to the previous smaller bar.

This is a classic application. When you pop an element `h` from an increasing stack, 
it means the current bar `curr_height` is shorter than `h`. This `curr_height` acts 
as the right boundary for a rectangle whose height is `h`. The left boundary is 
determined by the new `stack.top()` (the previous smaller element) or the beginning 
of the array if the stack becomes empty. The width of this rectangle would be 
`current_index - stack.top() - 1`.

#### Solution Walkthrough: Next Greater Element I (LeetCode)

**Problem Description (Simplified):**

You are given two arrays, `nums1` and `nums2`, where `nums1` is a subset of `nums2`. 
For each element in `nums1`, find its "next greater element" in `nums2`. The next 
greater element for an element `x` is the first element to its right in `nums2` 
that is greater than `x`. If it doesn't exist, return -1.

**Example:**
`nums1 = [4, 1, 2]`
`nums2 = [1, 3, 4, 2]`

**Output:** `[-1, 3, -1]`

* For `4` in `nums1`: In `nums2`, `4`'s right side elements are `2`. 
No element greater than `4`. So `-1`.
* For `1` in `nums1`: In `nums2`, `1`'s right side elements are `3, 4, 2`. 
The first greater element is `3`. So `3`.
* For `2` in `nums1`: In `nums2`, `2`'s right side elements are empty. 
No element greater than `2`. So `-1`.

**Algorithm Steps:**

1.  **Understand the core task:** We need to find the "next greater element to the 
right" for *all* elements in `nums2`. Once we have this mapping, we can just look 
up the values for elements present in `nums1`.

2.  **Data Structures:**
    * `stack`: A monotonic decreasing stack to store elements from `nums2`.
    * `next_greater_map`: A hash map (dictionary in Python) to store the 
    `element -> next_greater_element` mapping found in `nums2`.

3.  **Phase 1: Populate `next_greater_map` using `nums2` and a Monotonic Stack.**
    * Initialize `stack = []`
    * Initialize `next_greater_map = {}`
    * Iterate through `num` in `nums2`:
        * **While `stack` is not empty AND `stack.top()` is less than `num`:**
            * Pop `prev_element = stack.pop()`.
            * Store `prev_element -> num` in `next_greater_map`. (Because `num` 
            is the first element greater than `prev_element` to its right).
        * **Push `num` onto the `stack`.**

4.  **Phase 2: Construct the result for `nums1`.**
    * Initialize `result = []`
    * Iterate through `query_num` in `nums1`:
        * Look up `query_num` in `next_greater_map`.
        * If `query_num` is in `next_greater_map`, append its mapped value to `result`.
        * If `query_num` is *not* in `next_greater_map` (meaning it had no next 
        greater element in `nums2`), append `-1` to `result`.

5.  **Return `result`.**

#### Solution Walkthrough with `nums1 = [4, 1, 2]`, `nums2 = [1, 3, 4, 2]`

**Phase 1: Process `nums2 = [1, 3, 4, 2]`**

* `stack = []`
* `next_greater_map = {}`

1.  **`num = 1`:**
    * Stack is empty. Push 1. `stack = [1]`

2.  **`num = 3`:**
    * `stack.top() = 1`. `1 < 3`. Pop 1. `next_greater_map[1] = 3`. `stack = []`
    * Stack is empty. Push 3. `stack = [3]`

3.  **`num = 4`:**
    * `stack.top() = 3`. `3 < 4`. Pop 3. `next_greater_map[3] = 4`. `stack = []`
    * Stack is empty. Push 4. `stack = [4]`

4.  **`num = 2`:**
    * `stack.top() = 4`. `4 > 2`. Condition `stack.top() < num` is false.
    * Push 2. `stack = [4, 2]`

**End of Phase 1:**
* `stack = [4, 2]` (Elements 4 and 2 have no next greater element in `nums2`)
* `next_greater_map = {1: 3, 3: 4}`

**Phase 2: Process `nums1 = [4, 1, 2]`**

* `result = []`

1.  **`query_num = 4`:**
    * Is `4` in `next_greater_map`? No.
    * Append `-1` to `result`. `result = [-1]`

2.  **`query_num = 1`:**
    * Is `1` in `next_greater_map`? Yes, `next_greater_map[1] = 3`.
    * Append `3` to `result`. `result = [-1, 3]`

3.  **`query_num = 2`:**
    * Is `2` in `next_greater_map`? No.
    * Append `-1` to `result`. `result = [-1, 3, -1]`

**Final Result:** `[-1, 3, -1]`

This matches the example output.

#### Python Code Implementation:

```python
def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    Finds the next greater element for each element in nums1 within nums2.
    """
    stack = []  # Monotonic decreasing stack
    next_greater_map = {}  # Stores element -> its next greater element

    # Phase 1: Populate next_greater_map by iterating through nums2
    for num in nums2:
        # While the stack is not empty AND the current num is greater than the 
        # element at the top of the stack. This means num is the next greater 
        # element for stack.top()
        while stack and stack[-1] < num:
            popped_element = stack.pop()
            next_greater_map[popped_element] = num
        
        # Push the current num onto the stack.
        # It will either maintain the decreasing order or wait for a greater 
        # element to its right.
        stack.append(num)
    
    # After iterating through nums2, any elements remaining in the stack
    # do not have a next greater element to their right in nums2.
    # We don't strictly need to add them to the map with -1 here,
    # as the lookup in Phase 2 will handle missing keys by returning -1.
    # But for completeness:
    # while stack:
    #     next_greater_map[stack.pop()] = -1

    # Phase 2: Construct the result array for nums1 using the map
    result = []
    for query_num in nums1:
        # Get the next greater element from the map, default to -1 if not found
        result.append(next_greater_map.get(query_num, -1))
        
    return result

# Test cases
nums1_1 = [4, 1, 2]
nums2_1 = [1, 3, 4, 2]
print(f"Input: nums1={nums1_1}, nums2={nums2_1}")
print(f"Output: {nextGreaterElement(nums1_1, nums2_1)}") # Expected: [-1, 3, -1]

nums1_2 = [2, 4]
nums2_2 = [1, 2, 3, 4]
print(f"Input: nums1={nums1_2}, nums2={nums2_2}")
print(f"Output: {nextGreaterElement(nums1_2, nums2_2)}") # Expected: [3, -1]

nums1_3 = [1, 3, 5, 2, 4]
nums2_3 = [6, 5, 4, 3, 2, 1, 7]
print(f"Input: nums1={nums1_3}, nums2={nums2_3}")
print(f"Output: {nextGreaterElement(nums1_3, nums2_3)}") # Expected: [7, 7, 7, 7, 7]
```

#### Time and Space Complexity:

* **Time Complexity:** 
    * $O(N_2 + N_1)$ where $N_2$ is the length of `nums2` and $N_1$ is the
     length of `nums1`.
    * The first loop iterates through `nums2` once. Each element is pushed 
    onto and popped from the stack at most once. So, processing `nums2` 
    takes $O(N_2)$ time.
    * The second loop iterates through `nums1` once. Dictionary lookups take 
    $O(1)$ on average. So, processing `nums1` takes $O(N_1)$ time.
    * Total time complexity: $O(N_2 + N_1)$.

* **Space Complexity:** $O(N_2)$
    * In the worst case, the stack can store all elements of `nums2` 
    (e.g., if `nums2` is in decreasing order).
    * The `next_greater_map` can store up to $N_2$ key-value pairs.
    * Total space complexity: $O(N_2)$.

This solution is highly efficient due to the monotonic stack's ability to 
process relationships in a single pass.


-------------------------------------------------------------------------------------
### Q006 : Isomorphic arrays and strings in DSA;;

#### What Does "Isomorphic" Mean?

**"Isomorphic"** comes from Greek:

* *Iso* = same
* *Morph* = form or structure

So when we say two arrays or strings are *isomorphic*, we mean:

**NOTE:** They have the same structure or pattern, even if the actual characters 
or numbers differ.

---

#### Isomorphic Strings

for eg, 

```text
s = "egg"
t = "add"
```

They are isomorphic because mapping is consistent

* 'e' → 'a'
* 'g' → 'd'

#### Not Isomorphic:

```text
s = "foo"
t = "bar"
```

* 'o' maps to 'a' and then to 'r' → Inconsistent mapping

**Rule:** Each character in the first string must map to one and only one character 
in the second — and vice versa.

---

#### Isomorphic Arrays

Imagine:

```python
a = [1, 2, 1]
b = [9, 8, 9]
```

These are **isomorphic**, because:

* 1 → 9
* 2 → 8
* pattern `[1, 2, 1]` maps to `[9, 8, 9]`

But:

```python
a = [1, 2, 1]
b = [9, 8, 7]
```

**Not isomorphic** – because 1 maps to 9 *and later* to 7 → inconsistent

---

#### Python Code to Check Isomorphic Strings:

```python
def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    map_s_t = {}
    map_t_s = {}

    for ch1, ch2 in zip(s, t):
        if (ch1 in map_s_t and map_s_t[ch1] != ch2) or \
           (ch2 in map_t_s and map_t_s[ch2] != ch1):
            return False
        map_s_t[ch1] = ch2
        map_t_s[ch2] = ch1

    return True
```

---

#### Real-World Analogy:

Think of **isomorphic** like using the same *template* with different content.
E.g., both `"egg"` and `"add"` have the pattern `A B B`.

It’s like having two functions that behave the same way, just with different 
variable names.


-------------------------------------------------------------------------------------
### Q005 : Bitwise Manipulation in One Go

Bit manipulation is a powerful technique in competitive programming and DSA 
that often unlocks highly efficient o(1) or o(logn) solutions for problems 
that might otherwise seem to require more complex data structures or algorithms. 

It's about directly working with the binary representation of numbers.

The "hidden tricks" aren't really secrets, but rather patterns and properties 
of binary numbers that, once understood, become intuitive tools. Let's break 
down the core concepts, common operations, and then dive into these hidden 
tricks and problem patterns.

---

#### Core Concepts of Binary Numbers

Every integer can be represented in binary (base-2) using only 0s and 1s.

* **Bit:** A single binary digit (0 or 1).
* **MSB (Most Significant Bit):** The leftmost bit, representing the highest 
power of 2.
* **LSB (Least Significant Bit):** The rightmost bit, representing `2^0 = 1`.
* **Position:** Bits are indexed from right to left, starting at 0. So, the 
`ith bit (0-indexed)` represents `2^i`.

**Example:**

Decimal 13
Binary: `1101`
* Bit 0: `1` (1 x 2^0 = 1)
* Bit 1: `0` (0 x 2^1 = 0)
* Bit 2: `1` (1 x 2^2 = 4)
* Bit 3: `1` (1 x 2^3 = 8)

Total: 1 + 0 + 4 + 8 = 13

---

#### Basic Bitwise Operators

These are the fundamental building blocks.

1.  **AND (`&`)**:
    * Result bit is 1 if *both* corresponding bits are 1.
    
    * Example: `5 (0101) & 3 (0011) = 1 (0001)`
    * **Use cases:** Checking if a bit is set, masking bits.

2.  **OR (`|`)**:
    * Result bit is 1 if *at least one* corresponding bit is 1.
    
    * Example: `5 (0101) | 3 (0011) = 7 (0111)`
    * **Use cases:** Setting a bit, combining flags.

3.  **XOR (`^`)**:
    * Result bit is 1 if corresponding bits are *different*.
    
    * Example: `5 (0101) ^ 3 (0011) = 6 (0110)`
    * **Properties (very useful):**
        * `A ^ A = 0` (XORing a number with itself gives 0)
        * `A ^ 0 = A` (XORing with 0 gives the number itself)
        * XOR is commutative and associative: `(A ^ B) ^ C = A ^ (B ^ C)`
    * **Use cases:** Swapping numbers without a temp variable, finding single 
    unique element, detecting differences.

4.  **NOT (`~`)**: (Bitwise Complement)
    * Inverts all bits (0 becomes 1, 1 becomes 0).
    
    * Example: `~5 (~0101) = 1010` (This depends on integer size, usually 2's 
    complement for negative numbers).
    * **Caution:** In most languages, `~x` on a positive integer will result in a 
    negative integer due to 2's complement representation. For competitive 
    programming, it's often used with masks where its signed behavior isn't an issue.
    * **Use cases:** Creating masks.

5.  **Left Shift (`<<`)**:
    * `x << y`: Shifts bits of `x` left by `y` positions. Fills right with 0s.
    * Equivalent to multiplying by $2^y$.
    
    * Example: `5 (0101) << 1 = 10 (1010)`
    * **Use cases:** Multiplying by powers of 2, creating masks (`1 << i` gives a 
    number with only the $ith bit set).

6.  **Right Shift (`>>`)**:
    * `x >> y`: Shifts bits of `x` right by `y` positions.
    * Equivalent to integer division by 2^y.
    * **Arithmetic Right Shift (signed):** Most languages (Java, Python, C++) 
    perform arithmetic right shift for signed integers, meaning the sign bit 
    is propagated.
    * **Logical Right Shift (unsigned):** Fills left with 0s. (Python's `>>` is 
    arithmetic for signed, logical for unsigned. In C++, `>>` is arithmetic for 
    signed, logical for unsigned. Java `>>>` is logical).

    * Example: `10 (1010) >> 1 = 5 (0101)`
    * **Use cases:** Dividing by powers of 2, iterating through bits (getting 
    the ith bit).

---

#### Hidden Tricks and Common Patterns

These are the powerful applications that leverage the properties of bitwise 
operations.

#### 1. Checking if a Bit is Set

* **Trick:** `(num >> i) & 1` or `num & (1 << i)`
* **Explanation:**
    * `num & (1 << i)`: Creates a mask with only the $i$-th bit set. If `num` 
    also has the $ith bit set, the result of AND will be non-zero (specifically, 
    `1 << i`). Otherwise, it's 0.
    * `(num >> i) & 1`: Shifts the $i$-th bit to the 0-th position (LSB). Then 
    ANDs with 1. If the LSB is 1, result is 1; otherwise, 0.
* **Example:** Check if 2nd bit of 13 (01101) is set. 
`(13 >> 2) & 1` -> `(0011) & 1` -> `1`. Yes.

#### 2. Setting a Bit

* **Trick:** `num | (1 << i)`
* **Explanation:** Creates a mask with only the $i$-th bit set. ORing with `num` 
ensures that the $ith bit becomes 1, while other bits remain unchanged because 
(`X | 0 = X` and `X | 1 = 1`).

#### 3. Clearing/Unsetting a Bit

* **Trick:** `num & ~(1 << i)`
* **Explanation:**
    * `1 << i`: Mask with $i$-th bit set.
    * `~(1 << i)`: Inverts all bits. This creates a mask with all bits set except 
    the ith bit.
    * ANDing with `num` will keep all bits of `num` as they are, except for the 
    ith bit, which will become 0 (because `X & 0 = 0`).

#### 4. Toggling a Bit

* **Trick:** `num ^ (1 << i)`
* **Explanation:** `1 << i` creates a mask. XORing with it flips the $i$-th bit 
(`0^1=1`, `1^1=0`) while leaving others unchanged (`X^0=X`).

#### 5. Checking if a Number is a Power of 2

* **Trick:** `num > 0 and (num & (num - 1)) == 0`
* **Explanation:**
    * A power of 2 in binary has exactly one bit set 
    (e.g., 1 (0001), 2 (0010), 4 (0100), 8 (1000)).
    * `num - 1` will flip that set bit to 0 and all bits to its right to 1 
    (e.g., `8 (1000) - 1 = 7 (0111)`).
    * `num & (num - 1)` will therefore be 0 if `num` is a power of 2.
    * `num > 0` is essential to handle `0` correctly, as `0 & -1` is `0`.

#### 6. Counting Set Bits (Population Count / Hamming Weight)

* **Trick (Brian Kernighan's Algorithm):**
    ```python
    count = 0
    while num > 0:
        num &= (num - 1) # Clears the least significant set bit
        count += 1
    return count
    ```
* **Explanation:** `num & (num - 1)` is a magical operation. It clears the LSB 
(least significant bit) of `num`. For example:
    * `12 (1100)`
    * `12 - 1 = 11 (1011)`
    * `12 & 11 = 8 (1000)` (LSB of 12 was at pos 2, now cleared)
    * The loop continues until `num` becomes 0. The number of iterations is the 
    number of set bits.

* **Other ways:** Many languages have built-in functions 
(e.g., Python `bin(num).count('1')`, C++ `__builtin_popcount(num)`)

#### 7. Finding the Unique Element in an Array (where all others appear twice)

* **Trick:** XOR all elements together.
* **Explanation:** `A ^ A = 0` and `A ^ 0 = A`. Since all duplicate elements 
cancel each other out (`XOR` to 0), the unique element remains.
* **Example:** `[4, 1, 2, 1, 2]`
    `4 ^ 1 ^ 2 ^ 1 ^ 2`
    `= 4 ^ (1 ^ 1) ^ (2 ^ 2)`
    `= 4 ^ 0 ^ 0 = 4`

#### 8. Swapping Two Numbers

* **Trick:** `a = a ^ b; b = a ^ b; a = a ^ b;`

* **Explanation:**
    1.  `a = a ^ b`: `a` now holds the XOR sum of original `a` and `b`.
    2.  `b = a ^ b`: This is `(orig_a ^ orig_b) ^ orig_b`. 
    Since `orig_b ^ orig_b = 0`, `b` now becomes `orig_a`.
    3.  `a = a ^ b`: This is `(orig_a ^ orig_b) ^ orig_a`. 
    Since `orig_a ^ orig_a = 0`, `a` now becomes `orig_b`.

* **Caution:** Don't use if `a` and `b` refer to the same memory location 
(e.g., `a[i] = a[i] ^ a[j]; a[j] = ...`).

#### 9. Finding Two Unique Elements (where all others appear twice)

* **Trick:**
    1.  XOR all elements in the array. The result `xor_sum` will be 
    `unique1 ^ unique2`.
    2.  Find any set bit in `xor_sum` 
    (e.g., the rightmost set bit using `xor_sum & (-xor_sum)` in 2's 
    complement, or `xor_sum & (~xor_sum + 1)`). Let this be `mask`.
    3.  Divide all numbers in the original array into two groups: 
    those that have the `mask` bit set, and those that don't.
    4.  XOR all numbers in Group 1. The result will be `unique1`.
    5.  XOR all numbers in Group 2. The result will be `unique2`.

* **Explanation:** `unique1` and `unique2` must differ at least one bit 
position (otherwise they'd be the same number). The `mask` identifies one 
such differing bit. By grouping numbers based on this bit, you ensure 
`unique1` is in one group and `unique2` in the other. All other pairs of 
numbers (which appear twice) will have both instances in the same group, 
thus cancelling out.

#### 10. `x & (x - 1)` and `x & (~x + 1)` (or `x & -x`)

* `x & (x - 1)`: **Clears the LSB** (Least Significant Set Bit).
    - Example: `12 (1100) & 11 (1011) = 8 (1000)`

* `x & (~x + 1)` or `x & -x` (using 2's complement representation for `-x`): 
Isolates the LSB. Returns a number with only the LSB of `x` set.
    * Example: `12 (1100)`
        * `~12 = -13` (binary `0011` becomes `1100` if considering 4 bits, 
        then for negative numbers it's 2's complement)
        * In 2's complement, `-12` is `...1111110100`.
        * `12 & -12 = 4 (0100)` which is the LSB of 12.
    * This is incredibly useful for problems involving iterating through 
    subsets or finding the first differing bit.

#### 11. Converting Character to Lower/Upper Case

* **Trick:**

    * To lowercase: `char | ' '` 
    (OR with space character's ASCII value, which has the 5th bit set)

    * To uppercase: `char & '_' ` 
    (AND with underscore character's ASCII value, which has the 5th bit cleared)

* **Explanation:** The difference between ASCII uppercase and lowercase letters 
is exactly the 5th bit (0-indexed).

    * 'A' (65) = `01000001`
    * 'a' (97) = `01100001`
    * ' ' (32) = `00100000` (only 5th bit set)
    * '_' (95) = `01011111` (only 5th bit cleared, others set for relevant range)

* **Note:** This is less common in competitive programming than dedicated 
`$tolower/$toupper` functions, but demonstrates bitwise character manipulation.

#### 12. Bitmasks for Subsets

* **Trick:** Iterating through all subsets of a set of $N$ items.

* **Explanation:** A bitmask is an integer where each bit represents the presence 
or absence of an element. If you have $N$ elements, you can represent all $2^N$ 
subsets using integers from $0$ to $2^N - 1$.

* **Example:** For a set {A, B, C} (N=3):
    * `000` (0) -> {}
    * `001` (1) -> {C}
    * `010` (2) -> {B}
    * `011` (3) -> {B, C}
    * `100` (4) -> {A}
    * ...and so on.

* **Usage:**
    ```python
    for i in range(1 << N): # i iterates from 0 to 2^N - 1
        for j in range(N):
            if (i >> j) & 1: 
                # Check if j-th element is in the current subset (represented by i)
                # Element j is in the subset
    ```
* **Problems:** Subsets, combination sum variations, TSP (Traveling Salesperson 
Problem with dynamic programming and bitmask), Knapsack variations.

#### 13. Bitmask DP (Dynamic Programming with Bitmasks)

* **Trick:** Using an integer as the state in DP to represent a subset or combination 
of items/states.

* **Example:** TSP, problems where you need to visit all nodes, or select items with 
dependencies. `dp[mask]` could mean "the minimum cost to visit all nodes represented 
by set bits in `mask`".

---

#### General Tips for Bit Manipulation Problems:

1.  **Draw it out:** When stuck, write down numbers in binary. This helps visualize 
the effect of operations.
2.  **Powers of 2:** Remember `1 << i` is $2^i$.
3.  **LSB:** `x & -x` is a quick way to get the value of the LSB.
4.  **`~` operator caution:** Be aware of signed vs. unsigned integer representation, 
especially with `~` in C++/Java. Python handles large integers automatically, so `~` 
is usually safe but still represents two's complement.
5.  **Think about parity:** XOR is great for parity checks.
6.  **Immutable Integers:** Remember that bitwise operations return *new* integers; 
they don't modify the original in place.
7.  **Practice!** The more you see and solve problems, the more these tricks will 
become second nature.

Bit manipulation problems can be challenging because they require thinking in a 
different base, but mastering these tricks will significantly expand your DSA toolkit.


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