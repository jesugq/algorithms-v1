# 1433 Check If A String Can Break Another String

## Description

Given two strings: `s1` and `s2` with the same size, check if some permutation of a string `s1` can break some permutation of string `s2` or vice-versa (In other words `s2` can break `s1`).

A string `x` can break a string `y` (both of size `n`) if `x[i] >= y[i]` (in alphabetical order) for all `i` between 0 and `n-1`.

**Example 1** -

```bash
Input: s1 = "abc", s2 = "xya"
Output: true
Explanation: "ayx" is a permutation of s2 = "xya" which can break to string "abc" which is a permutation of s1 = "abc"
```

```bash
Input: s1 = "abe", s2 = "acd"
Output: false
Explanation: All permutation for s1 = "abe" are: "abe aeb bae bea eab eba" and all permutation for s2 = "acd" are: "acd adc cad cda dac dca". However, there is not any permutation which can break some permutation from s2 and vice-versa.
```

```bash
Input: s1 = "leetcode", s2 = "interview"
Output: true
```

## Theory

**Permutation** - A permutation, also called an "arrangement number", or "order", is a rearrangement of the elements of an ordered list S into a one-to-one correspondence with S itself. A string of length n! permutation.

The following are the permutations of string 'abc'. `abc acb bac bca cba cab`.

## Learnings

Naming conventions can still make or break a code. I opted for giving more importance to the object themselves, such as list1 or string2, instead of their purpose in the code.

I tried doing operations with ambiguous strings string1_sorted and string2_sorted, which only ended in confusing code. I opted to make the breaker and target strings, using additional memory to make the reader know exactly which string is supposed to break the other, after which the operations started making sense.
