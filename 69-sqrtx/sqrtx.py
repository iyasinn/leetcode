class Solution:
    # ALWAYS DO THE BRUTE FORCE 
    # THE BRUTE FORCE TEACHES YOU HOW TO DO THE ACTUAL SOLUTION
    # Looking for a number, you do SOLUTION SAPCE SEARCH 
    
    def mySqrt(self, x: int) -> int:

        root = 1 
        while (root * root < x): 
            root += 1

        if (root * root == x): 
            return root

        return root - 1