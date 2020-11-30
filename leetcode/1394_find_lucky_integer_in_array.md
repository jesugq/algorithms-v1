# 1394 Find Lucky Integer in an Array

## Description

Given an array of integers `arr`, a lucky integer is an integer which has a frequency in the array equal to its value.

Return a *lucky integer* in the array. If there are multiple lucky integers return the **largest** of them. If there is no lucky integer return **-1**.

**Example 1:** -

```text
Input: arr = [2, 2, 3, 4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
```

**Example 2:** -

```text
Input: arr = [1, 2, 2, 3, 3, 3]
Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
```

**Example 3:** -

```text
Input: arr = [2, 2, 2, 3, 3]
Output: -1
Explanation: There are no lucky numbers in the array.
```

**Example 4:** -

```text
Input: arr = [5]
Output: -1
```

**Example 5:** -

```text
Input: arr = [7, 7, 7, 7, 7, 7, 7]
Output: 7
```

**Contraints:** -

- `1 <= arr.length <= 500`
- `1 <= arr[i] <= 500`


## Learnings

Initialization for multi-threading A.K.A. Leetcode submissions is a confusing subject, so I've chosen to reduce the flexibility of my initialization methods by not accepting any variables. This'll make sure the class is initialized only the way it should be, with all empty values.