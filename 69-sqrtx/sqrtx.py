class Solution:
    # ALWAYS DO THE BRUTE FORCE 
    # THE BRUTE FORCE TEACHES YOU HOW TO DO THE ACTUAL SOLUTION
    # Looking for a number, you do SOLUTION SAPCE SEARCH 

    def mySqrt(self, x: int) -> int:

        # [start, end]
        start = 0
        end = x

        while (start <= end): 

            mid = (end + start) // 2 
            square = mid * mid 

            if (square < x):
                start = mid + 1
            elif (square > x): 
                end = mid - 1
            else: 
                return mid
        
        return end