class Solution:
    def mySqrt(self, x: int) -> int:
        root = 1 
        while (root * root < x): 
            root += 1
            
        if (root * root == x): 
            return root

        return root - 1