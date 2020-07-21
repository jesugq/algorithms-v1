# 14 Longest Common Prefix

## Description

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

**Example 1** -

```bash
Input: ["flower", "flow", "flight"]
Output: "fl"
```

**Example 2** -

```bash
Input: ["dog", "racecar", "car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

**Note** - All given inputs are in lowercase letters `a-z`

## Learnings

Something I remembered is that I find it easiest to read my code when I use a specific name notation, in the form of `context_responsibility`, where

- _Context_ refers to the group in which this variable belongs to, e.g. the prefix answer, the character analyzed or the array being iterated over.
- _Responsibility_ refers to the delegated task this variable is in charge of, e.g. being the longest prefix, the current character or the shortest word or length of an array.

Hopefully, these naming conventions make it easy for my future coworkers to be able to read my code as well. I recall good code is not necessarily one that does it in the least amount of lines, but one that is maintainable.

> John Woods
>
> Always code as if the guy who ends up maintaining your code will be a violent psycopath who knows where you live.
