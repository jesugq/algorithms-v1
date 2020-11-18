# 1365 How Many Numbers Are Smaller Than The Current Number

## Description

Given the array `nums`, for each `nums[i]` find out how many numbers in the array are smaller than it. That is, for each `nums[i]` you have to count the number of valid `j's` such that `j != i` and `nums[j] < nums[i]`

Return the answer in an array.

**Example 1** -

```bash
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation:
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2, and 3).
For nums[1]=1 does not exist any number smaller than it.
For nums[2]=2 there exist one smaller noumber than it (1).
For nums[3]=2 there exist one smaller number than it (1).
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
```

**Example 2** -

```bash
Input: nums = [6,5,4,8]
Output: [2,1,0,3]
```

**Example 3** -

```bash
Input: nums = [7,7,7,7]
Output: [0,0,0,0]
```

## Learning

```java
// commonNumbers    [8, 1, 2, 2, 3]

// sortedNumbers    [1, 2, 2, 3, 8]
// repeatedNumbers  [0, 1, 1, 0, 0]
// smallerNumbers   [0, 1, 1, 3, 4]

// smallerNumbers   Highest Index on SortedNumbers - repeatedNumbers[i]
// smallerNumbers   [0-0, 1-1, 1-1, 3-0, 8-0]

// smallerNumbers   Lowest Index on SortedNumbers
// smallerNumbers   [0, 1, 1, 3, 4]
```

The first thing I noticed is how I was going to make the correct algorithm for the system. Using just the 'commonNumbers' would be a pain as they are unsorted, so I would prefer sorting them for the following operations.

Afterwards I thought of using a system where the amount of numbers smaller is the highest index of the number in the sorted array. But this would require accounting for the repeated numbers, as seen in `[...2, 2...]`. After failing to make an algorithm to count the times a number was repeated on an array, I figured I would not need it if I instead just used the *lowest* index of the number in the sorted array.

After having the algorithm ready I had to debug what essentially was nothing. That's right, I debugged nothing because I forgot you cannot print arrays as-is with a `System.out.println()` the way you would `print()` in Python. I have been hand-held by that programming language.

The code looks clean and it actually helped me make the algorithm to write in 'well-written pose'. I would create the functions that needed to be called and wrote them later, as I needed them. I even made my first *manual* refactor (God knows how to refactor code in VSCode), and it was great but not so much necessary.

For a simple algorithm (according to Leetcode) I took a fair bit of time. Here's to hoping I don't get too rusty, perhaps I even get my first job soon.
