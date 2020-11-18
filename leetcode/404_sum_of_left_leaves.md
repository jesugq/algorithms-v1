# 404 Sum of Left Leaves

## Description

Find the sum of all left leaves in a given binary tree.

**Example 1:** -

```text
        3
      /   \
    9       20
          /    \
        15      17

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
```

**Example 2:** -

```text
            1
          /   \
        2       3
      /   \
    4       5
```

## Learnings

I got stuck in this one and I'm not sure why. At first I tried to do some kind of weird algorithm where I kept tagging the value `leftLeaveSum` along in every recursion, which did not end up well, as it was overwritten somewhere in the process, because it was never set to be returned alone.

Then I tried making the return value be the `leftLeaveSum` itself, but I made the design mistake of trying to access children's values from their parents, and got some ugly code. It got the correct answer, except for the fact that I considered every left node a 'leaf', and the definition of a leaf is a **node with no children**.

On the last iteration I realized I could just send a value from the parent to the children, telling them if they were a left child, so that they could then see if they fit the criteria to add their value to the now non-existent `leftLeaveSum`. Not only this code was the cleanest of the bunch, it was the only correct one, except when asked if a root leaf is a left child, which it wrongly considered itself to be.

I'm still learning.
