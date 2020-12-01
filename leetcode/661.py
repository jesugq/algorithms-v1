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