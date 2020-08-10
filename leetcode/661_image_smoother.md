# 661 Image Smoother

## Description

Given a 2D integer matrix M representing the gray scale of an image, you need to design a moother to make th egray scale of each cell become the average gray scale (rounding down) of all of the 8 sorrounding cells and itself. If a cell has less than 8 sorrounding cells, then use as many as you can.

**Example 1** -

```bash
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0,0,0],
 [0,0,0],
 [0,0,0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): Floor(3/4) = Floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): Floor(5/6) = Floor(0.8333) = 0
For the point (1,1): Floor (8/9), = Floor (0.8889) = 0
```

Note:

1. The value in the given matrix is in the range of [0, 255].
2. The length and width of the given matrix are in the range of [1, 150].

## Learnings

Apparently, in Python you can go out of bounds in a List or a Matrix (List of Lists). If you were to access the position `[-1][-1]` of a matrix, you'd actually get a value, which is the last element (As if the Matrix carried over). While this functionality is welcome, it was a surprise nonetheless.

So instead of lazily relying on an IndexError exception, it was necessary to specify to the code to keep the adjacent cell average calculation to stay within bounds, which was not hard at all.

Also, when dealing with objects, it is of upmost importance to create an independent copy if both items will be used for a different purpose. Both the source and the result matrix were updated upon calculation. Creating a copy of a matrix in a single line is as follows.

> https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array-in-python
>
> ```python
> # Creates a list containing 5 lists, each of 8 items, all set to 0
> w, h = 8, 5;
> Matrix = [[0 for x in range(w)] for y in range(h)]
> ```
