class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_mark = [0] * len(mat)
        col_mark = [0] * len(mat[0])
        count = 0

        for i, row in enumerate(mat): 
            for j, num in enumerate(row): 
                if num == 1: 
                    row_mark[i] += 1
                    col_mark[j] += 1


        for i, row in enumerate(mat): 
            for j, num in enumerate(row): 
                if num == 1 and row_mark[i] == 1 and col_mark[j] == 1: 
                    count += 1
  

        return count



