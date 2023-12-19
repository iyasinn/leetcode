class Solution:

    def in_bounds(self, row, col, max_row, max_col): 
        return row >= 0 and row < max_row and col >= 0 and col < max_col

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        output = [[0] * len(img[0]) for _ in range(len(img))]

        for row_idx, row in enumerate(img): 
            for col_idx, num in enumerate(row): 

                avg = num 
                n = 1
                row_diff = [-1, -1, 0, 1, 1, 1, 0, -1]
                col_diff = [0, 1, 1, 1, 0, -1, -1, -1]
                
                for i in range(len(row_diff)): 
                    if not self.in_bounds(row_idx + row_diff[i], col_idx + col_diff[i], len(img), len(img[0])):
                        continue
                    avg += img[row_idx + row_diff[i]][col_idx + col_diff[i]]
                    n += 1
                
                output[row_idx][col_idx] = floor(avg / n)
        
        return output











