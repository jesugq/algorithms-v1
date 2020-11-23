# 1022 Sum of Root To Leaf Binary Numbers

## Description

You are given the `root` of a binary tree where each node has a value `0` or `1`. Each root-to-leaf path represents a binary number starting with the most significant bit. For example, if the path is `0 -> 1 -> 1 -> 0 -> 1`, then this could represent `01101` in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers. The answer is **guaranteed** to fit in a **32-bits** integer.

**Example 1:** -

```text
        1
      /   \
    0       1
   / \     / \
  0   1   0   1

Input: root = [1, 0, 1, 0, 1, 0, 1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
```

**Example 2:** -

```text
Input: root = [0]
Output: 0
```

**Example 3:** -

```text
Input: root = [1]
Output: 1
```

**Example 4:** -

```text
Input: [1, 1]
Output: 3
```

**Constraints:** -

- The number of nodes in the tree is in the range [1, 1000].
- `Node.val` is `0` or `1`.

## Learnings

Writing clean code in Python proved to be hard because of one simple condition, all class methods should have the self parameter and be called with the self prefix. This makes code less readable than expected.

At least I did make clean code. I used to make just clean variables, and dumping everything into one big function. Needless to say, it ended up being terribly ugly.

Just take a look at this.

```python
from typing import List
import copy
import math

class Solution:
    def calc_matrix_adjacent(self, source_matrix, matrix_rows, matrix_cols, index, jndex) -> int:
        grayscale_sum = 0.0
        grayscale_items = 0

        for mndex in range(-1, 2):
            if 0 <= index + mndex < matrix_rows:
                for nndex in range(-1, 2):
                    if 0 <= jndex + nndex < matrix_cols:
                        grayscale_sum += source_matrix[index + mndex][jndex + nndex]
                        grayscale_items += 1
        
        return grayscale_sum, grayscale_items

    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        source_matrix = M
        matrix_rows = len(source_matrix)
        matrix_cols = len(source_matrix[0])
        result_matrix = [[0 for x in range(matrix_cols)] for y in range(matrix_rows)]

        for index in range(matrix_rows):
            for jndex in range(matrix_cols):
                grayscale_sum, grayscale_items = self.calc_matrix_adjacent(source_matrix, matrix_rows, matrix_cols, index, jndex)
                result_matrix[index][jndex] = math.floor(grayscale_sum / grayscale_items)

        return result_matrix
```

What are those? Sound effect included.