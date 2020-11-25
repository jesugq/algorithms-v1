# 257 Binary Tree Paths

## Description

Given a binary tree, return all root-to-leaf paths.

**Note:** A leaf is a node with no children.

**Example:** -

```text
Input:
        1
      /   \
    2       3
     \
      5

Output: ["1->2->5", "1->3"]
Explanation: All root-to-leaf paths are: 1->2->5, 1->3
```

## Learnings

This had no reason to be this hard. I had to resort to a global variable, which Leetcode does not support, to be able to create the List in the way it's supposed to. Something about using either simple addition `list1 + list2` or append `lists.append(list1) _ lists.append(list2)` does not create the correct structure for the result. I may need to delve further into recursion to prevent these from happening again.

Another thing I noticed is that my Solution classes are doing way too much. It has to manipulate the data structure in its entirety, and thus requires all knowledge of how the data structure works. This would be fine if it was some kind of mediator, but it also has to handle the logic to solve the algorithm. You cannot modify the object given to you to work with.
