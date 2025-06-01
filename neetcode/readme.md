````
-------------------------------------------------------------------------------------
-> Title : NEETCODE MASTER DSA NOTES    
-> Author : @neeraj-singh-jr
-> Status : Ongoing...
-> Created : 2024-03-17
-> Updated : 2024-06-17
-> Summary : Notes indices are as follows (**** pending)
-------------------------------------------------------------------------------------
-> Q008 : Boyer Moorie Algorithm In-Depth;;
-> Q007 : Monotonic Stacks Algorithms In-Depth;;
-> Q006 : Isomorphich arrays and strings in DSA;;
-> Q005 : Bitwise Manipulation in One Go;;
-> Q004 : Usage of 2^n combination for substring or subsequence problem;;
-> Q003 : Anagram in DSA Problems;;
-> Q002 : Pallindrome in DSA Problems;;
-> Q001 : Subarray and Subsequence in DSA Problems;;
-------------------------------------------------------------------------------------
````

### NEETCODE MASTER DSA NOTES : BEGINNING

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
### Q006 : Isomorphich arrays and strings in DSA;;

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