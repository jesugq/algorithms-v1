# 852 Peak Index in a Mountain Array

## Description

Let's call an array `arr` a **mountain** if the following properties hold:

- `arr.length >= 3`
- There exists some `i` with `0 < i < arr.length - 1` such that:
  - `arr[0] < arr[1] < ... arr[i-1] < arr[i]`
  - `arr[i] > arr[i+1] > ... > arr[arr.length - 1]`

Given an integer array `arr` that is **guaranteed** to be a mountain, return any `i` such that `arr[0] < arr[1] < ... arr[i-1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`.

**Example 1:** -

```text
Input: arr = [0,1,0]
Output: 1
```

**Example 2:** -

```text
Input: arr = [0,2,1,0]
Output: 1
```

**Example 3:** -

```text
Input: arr = [0,10,5,2]
Output: 1
```

**Example 4:** -

```text
Input: arr = [3,4,5,1]
Output: 2
```

**Example 5:** -

```text
Input: arr = [24,69,100,99,79,78,67,36,26,19]
Output: 2
```

## Learnings

I remembered to use private methods in the class when those methods need not to be accessed by outside classes. While I won't be fixing the past methods in all of my exercises, I will take that into consideration. This is something I realized when reading Clean Code. Sometimes too much transparency makes your class work like a data structure, when it should be the opposite, just enough transparency to be usable, but not to tell other classes how your internals are.