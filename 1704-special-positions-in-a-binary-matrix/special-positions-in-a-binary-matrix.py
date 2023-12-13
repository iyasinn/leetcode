class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_mark = [0] * len(mat)
        col_mark = [0] * len(mat[0])
        count = 0

        for i, row in enumerate(mat): 
            for j, num in enumerate(row): 
                row_mark[i] += num
                col_mark[j] += num

        for i, row in enumerate(mat): 
            for j, num in enumerate(row): 
                if num == row_mark[i] == col_mark[j] == 1: 
                    count += 1
  
        return count