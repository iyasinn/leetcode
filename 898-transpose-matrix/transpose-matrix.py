
# Teaching me to do a cool traversal 
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        output = [[0] * len(matrix) for _ in range(len(matrix[0]))]

        for col in range(len(matrix[0])):
            for row in range(len(matrix)): 

                output[col][row] = matrix[row][col]

        return output