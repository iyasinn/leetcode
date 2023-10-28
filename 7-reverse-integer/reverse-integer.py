class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        
        negative = x[0] == '-'
        # String slicing in reverse means start and end are reversed
        x = '-' + x[:0:-1] if negative else x[::-1]

        if float(x) < -2147483648.0 or float(x) > 2147483647.0: 
            return 0
        return int(x)

